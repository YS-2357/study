"""OCR an image folder into Markdown.

This script is intentionally generic. Put one-off event/session mappings under
raw/ so they stay local-only and can be discarded after processing.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, time
from pathlib import Path

import cv2
import pytesseract
from PIL import Image


@dataclass(frozen=True)
class Session:
    group: str
    title: str
    start: time
    end: time
    file_name: str | None = None


@dataclass(frozen=True)
class OcrResult:
    image: Path
    captured_at: datetime | None
    text: str
    layout_text: str
    confidence: float
    status: str


def parse_clock(value: str) -> time:
    return datetime.strptime(value, "%H:%M").time()


def parse_capture_time(path: Path) -> datetime | None:
    match = re.search(r"(\d{8})_(\d{6})", path.stem)
    if not match:
        return None
    return datetime.strptime("".join(match.groups()), "%Y%m%d%H%M%S")


def find_tesseract() -> str | None:
    found = shutil.which("tesseract")
    if found:
        return found

    for candidate in [
        Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe"),
        Path(r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"),
        Path.home() / r"AppData\Local\Programs\Tesseract-OCR\tesseract.exe",
    ]:
        if candidate.exists():
            return str(candidate)
    return None


def preprocess_image(path: Path, max_dimension: int) -> Image.Image:
    image = cv2.imread(str(path))
    if image is None:
        raise ValueError(f"Cannot read image: {path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape
    largest = max(height, width)
    if max_dimension > 0 and largest > max_dimension:
        scale = max_dimension / largest
        gray = cv2.resize(gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

    gray = cv2.bilateralFilter(gray, 7, 50, 50)
    gray = cv2.convertScaleAbs(gray, alpha=1.25, beta=8)
    return Image.fromarray(gray)


def normalize_text(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        clean = re.sub(r"\s+", " ", line).strip()
        if clean:
            lines.append(clean)
    return "\n".join(lines)


def layout_text_from_data(data: dict[str, list], include_low_confidence: bool) -> str:
    lines: dict[tuple[int, int, int], dict[str, object]] = {}
    item_count = len(data.get("text", []))
    for index in range(item_count):
        word = data["text"][index].strip()
        if not word:
            continue
        try:
            confidence = float(data["conf"][index])
        except ValueError:
            confidence = -1.0
        if confidence < 0:
            continue
        if not include_low_confidence and confidence < 35:
            continue

        key = (
            int(data["block_num"][index]),
            int(data["par_num"][index]),
            int(data["line_num"][index]),
        )
        entry = lines.setdefault(
            key,
            {
                "top": int(data["top"][index]),
                "left": int(data["left"][index]),
                "words": [],
            },
        )
        entry["top"] = min(int(entry["top"]), int(data["top"][index]))
        entry["left"] = min(int(entry["left"]), int(data["left"][index]))
        entry["words"].append((int(data["left"][index]), word))

    ordered_lines = sorted(
        lines.values(),
        key=lambda entry: (int(entry["top"]), int(entry["left"])),
    )
    output_lines: list[str] = []
    previous_top: int | None = None
    for entry in ordered_lines:
        top = int(entry["top"])
        if previous_top is not None and top - previous_top > 45 and output_lines:
            output_lines.append("")
        words = [word for _, word in sorted(entry["words"], key=lambda item: item[0])]
        line = normalize_text(" ".join(words))
        if line:
            output_lines.append(line)
        previous_top = top

    return "\n".join(output_lines)


def ocr_image(
    path: Path,
    lang: str,
    min_chars: int,
    min_confidence: float,
    tessdata_dir: Path | None,
    max_dimension: int,
    psm: int,
    include_low_confidence: bool,
) -> OcrResult:
    image = preprocess_image(path, max_dimension)
    config = f"--oem 3 --psm {psm}"
    if tessdata_dir is not None:
        config = f"{config} --tessdata-dir {tessdata_dir.resolve().as_posix()}"
    data = pytesseract.image_to_data(
        image,
        lang=lang,
        config=config,
        output_type=pytesseract.Output.DICT,
    )

    words: list[str] = []
    confidences: list[float] = []
    for word, confidence in zip(data.get("text", []), data.get("conf", [])):
        word = word.strip()
        if not word:
            continue
        try:
            numeric_confidence = float(confidence)
        except ValueError:
            continue
        if numeric_confidence >= 0:
            confidences.append(numeric_confidence)
        words.append(word)

    text = normalize_text(" ".join(words))
    layout_text = layout_text_from_data(data, include_low_confidence)
    average_confidence = sum(confidences) / len(confidences) if confidences else 0.0
    if len(text) < min_chars:
        status = "empty"
    elif average_confidence < min_confidence:
        status = "low_confidence"
    else:
        status = "usable"

    return OcrResult(path, parse_capture_time(path), text, layout_text, average_confidence, status)


def load_sessions(path: Path | None) -> list[Session]:
    if path is None:
        return []

    payload = json.loads(path.read_text(encoding="utf-8"))
    sessions = payload.get("sessions", payload)
    return [
        Session(
            group=item.get("group", "Sessions"),
            title=item["title"],
            start=parse_clock(item["start"]),
            end=parse_clock(item["end"]),
            file_name=item.get("file"),
        )
        for item in sessions
    ]


def session_for(result: OcrResult, sessions: list[Session]) -> Session | None:
    if result.captured_at is None:
        return None
    captured = result.captured_at.time()
    for session in sessions:
        if session.start <= captured < session.end:
            return session
    return None


def markdown_block(result: OcrResult, skip_empty: bool, skip_low_confidence: bool) -> str:
    if skip_empty and result.status == "empty":
        return "_OCR text omitted: empty / low-signal image._"
    if skip_low_confidence and result.status == "low_confidence":
        return "_OCR text omitted: low confidence. Review the image manually or try another OCR mode._"
    if not result.text:
        return "_No meaningful OCR text._"
    return "\n".join(f"> {line}" for line in result.text.splitlines())


def fenced_layout_block(result: OcrResult) -> str:
    text = result.layout_text or result.text
    if not text:
        return "_No meaningful OCR text._"
    return f"```text\n{text}\n```"


def image_lines(
    result: OcrResult,
    skip_empty: bool,
    skip_low_confidence: bool,
    preserve_layout: bool,
    heading_level: int,
) -> list[str]:
    heading = "#" * heading_level
    captured = result.captured_at.strftime("%H:%M:%S") if result.captured_at else "unknown"
    body = (
        fenced_layout_block(result)
        if preserve_layout
        else markdown_block(result, skip_empty, skip_low_confidence)
    )
    return [
        f"{heading} {result.image.name} ({captured})",
        f"- Status: `{result.status}`",
        f"- Confidence: `{result.confidence:.1f}`",
        "",
        body,
        "",
    ]


def write_flat_markdown(
    lines: list[str],
    results: list[OcrResult],
    skip_empty: bool,
    skip_low_confidence: bool,
    preserve_layout: bool,
) -> None:
    lines.extend(["## Images", ""])
    for result in results:
        lines.extend(image_lines(result, skip_empty, skip_low_confidence, preserve_layout, 3))


def write_session_markdown(
    lines: list[str],
    results: list[OcrResult],
    sessions: list[Session],
    skip_empty: bool,
    skip_low_confidence: bool,
    preserve_layout: bool,
) -> None:
    grouped: dict[Session | None, list[OcrResult]] = {session: [] for session in sessions}
    grouped[None] = []
    for result in results:
        grouped[session_for(result, sessions)].append(result)

    current_group: str | None = None
    for session in sessions:
        session_results = grouped.get(session, [])
        if not session_results:
            continue
        if session.group != current_group:
            lines.extend([f"## {session.group}", ""])
            current_group = session.group
        lines.extend(
            [
                f"### {session.title}",
                f"#### {session.start.strftime('%H:%M')}-{session.end.strftime('%H:%M')}",
                "",
            ]
        )
        for result in session_results:
            lines.extend(image_lines(result, skip_empty, skip_low_confidence, preserve_layout, 5))

    unassigned = grouped.get(None, [])
    if unassigned:
        lines.extend(["## Unassigned / Transition", ""])
        for result in unassigned:
            lines.extend(image_lines(result, skip_empty, skip_low_confidence, preserve_layout, 3))


def write_markdown(
    output_path: Path,
    image_dir: Path,
    results: list[OcrResult],
    sessions: list[Session],
    lang: str,
    title: str,
    skip_empty: bool,
    skip_low_confidence: bool,
    preserve_layout: bool,
) -> None:
    lines = [
        f"# {title}",
        "",
        "## Source",
        f"- Images: `{image_dir.as_posix()}`",
        "- Generated from filename timestamps when available",
        f"- OCR languages: `{lang}`",
        "",
    ]

    if sessions:
        write_session_markdown(lines, results, sessions, skip_empty, skip_low_confidence, preserve_layout)
    else:
        write_flat_markdown(lines, results, skip_empty, skip_low_confidence, preserve_layout)

    counts = {
        status: sum(1 for result in results if result.status == status)
        for status in ["usable", "low_confidence", "empty"]
    }
    lines.extend(
        [
            "## OCR Summary",
            f"- Images processed: {len(results)}",
            f"- Usable: {counts['usable']}",
            f"- Low confidence: {counts['low_confidence']}",
            f"- Empty / low signal: {counts['empty']}",
            "",
        ]
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def slugify(value: str, fallback: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or fallback


def session_filename(index: int, session: Session) -> str:
    if session.file_name:
        return session.file_name
    base = slugify(f"{session.group}-{session.title}", f"session-{index:02d}")
    return f"{index:02d}-{base}.md"


def write_split_by_session(
    output_dir: Path,
    image_dir: Path,
    results: list[OcrResult],
    sessions: list[Session],
    lang: str,
    title: str,
    skip_empty: bool,
    skip_low_confidence: bool,
    preserve_layout: bool,
) -> None:
    if not sessions:
        raise SystemExit("--split-by-session requires --sessions")

    grouped: dict[Session | None, list[OcrResult]] = {session: [] for session in sessions}
    grouped[None] = []
    for result in results:
        grouped[session_for(result, sessions)].append(result)

    output_dir.mkdir(parents=True, exist_ok=True)
    for index, session in enumerate(sessions, start=1):
        session_results = grouped.get(session, [])
        if not session_results:
            continue
        output_path = output_dir / session_filename(index, session)
        write_markdown(
            output_path,
            image_dir,
            session_results,
            [session],
            lang,
            f"{title} - {session.title}",
            skip_empty,
            skip_low_confidence,
            preserve_layout,
        )

    unassigned = grouped.get(None, [])
    if unassigned:
        write_markdown(
            output_dir / "99-unassigned.md",
            image_dir,
            unassigned,
            [],
            lang,
            f"{title} - Unassigned",
            skip_empty,
            skip_low_confidence,
            preserve_layout,
        )


def filter_images(
    images: list[Path],
    start_time: time | None,
    end_time: time | None,
    limit: int | None,
) -> list[Path]:
    filtered: list[Path] = []
    for image in images:
        captured_at = parse_capture_time(image)
        if captured_at is not None:
            captured = captured_at.time()
            if start_time is not None and captured < start_time:
                continue
            if end_time is not None and captured >= end_time:
                continue
        elif start_time is not None or end_time is not None:
            continue
        filtered.append(image)
        if limit is not None and len(filtered) >= limit:
            break
    return filtered


def main() -> int:
    parser = argparse.ArgumentParser(description="OCR JPG/PNG images into Markdown.")
    parser.add_argument("image_dir", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--sessions", type=Path, help="Optional raw-local JSON session mapping.")
    parser.add_argument("--title", default="OCR Output")
    parser.add_argument("--lang", default="kor+eng")
    parser.add_argument("--tessdata-dir", type=Path, help="Optional directory containing .traineddata files.")
    parser.add_argument("--start-time", type=parse_clock, help="Only OCR images at or after HH:MM.")
    parser.add_argument("--end-time", type=parse_clock, help="Only OCR images before HH:MM.")
    parser.add_argument("--limit", type=int, help="Maximum number of images to process after filtering.")
    parser.add_argument("--max-dimension", type=int, default=2200, help="Downscale images whose longest side exceeds this value. Use 0 to disable.")
    parser.add_argument("--psm", type=int, default=11, help="Tesseract page segmentation mode.")
    parser.add_argument("--min-chars", type=int, default=12)
    parser.add_argument("--min-confidence", type=float, default=35.0)
    parser.add_argument("--skip-empty", action="store_true", help="Omit body text for empty / low-signal images.")
    parser.add_argument("--skip-low-confidence", action="store_true", help="Omit body text for low-confidence OCR results.")
    parser.add_argument("--include-low-confidence", action="store_true", help="Include low-confidence words in layout-preserving output.")
    parser.add_argument("--preserve-layout", action="store_true", help="Reconstruct OCR by block/paragraph/line instead of one text stream.")
    parser.add_argument("--split-by-session", action="store_true", help="Write one Markdown file per configured session.")
    args = parser.parse_args()
    if args.split_by_session and args.output_dir is None:
        raise SystemExit("--split-by-session requires --output-dir")
    if not args.split_by_session and args.output is None:
        raise SystemExit("--output is required unless --split-by-session is used")

    tesseract = find_tesseract()
    if not tesseract:
        raise SystemExit("tesseract executable not found. Install Tesseract OCR and retry.")
    pytesseract.pytesseract.tesseract_cmd = tesseract

    images = sorted(
        [*args.image_dir.glob("*.jpg"), *args.image_dir.glob("*.jpeg"), *args.image_dir.glob("*.png")],
        key=lambda path: (parse_capture_time(path) or datetime.min, path.name),
    )
    if not images:
        raise SystemExit(f"No JPG/PNG images found under {args.image_dir}")
    images = filter_images(images, args.start_time, args.end_time, args.limit)
    if not images:
        raise SystemExit("No images matched the selected time window.")

    sessions = load_sessions(args.sessions)
    results = [
        ocr_image(
            path,
            args.lang,
            args.min_chars,
            args.min_confidence,
            args.tessdata_dir,
            args.max_dimension,
            args.psm,
            args.include_low_confidence,
        )
        for path in images
    ]
    if args.split_by_session:
        write_split_by_session(
            args.output_dir,
            args.image_dir,
            results,
            sessions,
            args.lang,
            args.title,
            args.skip_empty,
            args.skip_low_confidence,
            args.preserve_layout,
        )
    else:
        write_markdown(
            args.output,
            args.image_dir,
            results,
            sessions,
            args.lang,
            args.title,
            args.skip_empty,
            args.skip_low_confidence,
            args.preserve_layout,
        )

    usable = sum(1 for result in results if result.status == "usable")
    low = sum(1 for result in results if result.status == "low_confidence")
    empty = sum(1 for result in results if result.status == "empty")
    print(f"Processed {len(results)} images: usable={usable}, low_confidence={low}, empty={empty}")
    if args.split_by_session:
        print(f"Wrote session files under {args.output_dir}")
    else:
        print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
