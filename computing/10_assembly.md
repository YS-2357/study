---
tags:
  - computing
created_at: 2026-04-19T00:59:49
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_computing_overview.md)

# Assembly

## What It Is

Assembly is a low-level language where each instruction maps almost 1:1 to a single CPU machine instruction, written with human-readable mnemonics (`mov`, `add`, `jmp`) instead of raw binary.

## Analogy

Assembly is **phonetic spelling for the CPU**. Machine code is what the processor actually "speaks" — raw bytes like `48 c7 c0 01 00 00 00`. Assembly writes that same utterance as `mov rax, 1` — pronounceable letters instead of opaque hex. Every assembly line is one "sound" the CPU will make, and the assembler is the pronunciation guide that converts between the two forms.

## How It Works

### The Translation Chain

```
High-level (Python, Go, C)   ← you write here
       ↓ compiler
Assembly (arch-specific text) ← readable CPU instructions
       ↓ assembler
Machine code (binary bytes)   ← what the CPU executes
```

Assembly is a thin text layer over machine code. The assembler turns `mov rax, 1` into bytes like `48 c7 c0 01 00 00 00`.

### Core Building Blocks

| Concept | What it is |
|---|---|
| **Register** | Small, fast named slot inside the CPU (`rax`, `rbx`, `x0`, `sp`) |
| **Mnemonic** | Operation name (`mov`, `add`, `jmp`, `call`, `ret`) |
| **Operand** | Input to an instruction — register, immediate value, or memory address |
| **Label** | Named location for jumps/calls (`loop:`, `main:`) |
| **Directive** | Assembler instruction, not CPU instruction (`.text`, `.global`) |

### Architecture-Specific

Assembly is not portable — each [CPU architecture](./01_architecture.md) has its own instruction set:

| Architecture | Syntax examples |
|---|---|
| **x86-64** (Intel/AMD) | `mov rax, 1` (Intel) or `movq $1, %rax` (AT&T) |
| **ARM64** (Graviton, Apple Silicon) | `mov x0, #1` |
| **RISC-V** | `li a0, 1` |

Same logical operation, three different spellings. Recompilation is required to move between them.

### Why Two x86 Syntaxes?

x86 has two assembly dialects — **Intel** (`mov dst, src`) and **AT&T** (`mov src, dst`, registers prefixed with `%`). GCC/Clang default to AT&T; most modern tutorials and Windows tooling use Intel. They assemble to identical bytes.

## Example

A C function and its x86-64 assembly (Intel syntax):

```c
int add_one(int x) {
    return x + 1;
}
```

Compiled with `gcc -S -masm=intel -O1`:

```asm
add_one:
    lea eax, [rdi + 1]   ; eax = rdi + 1  (rdi holds x by calling convention)
    ret                  ; return; eax holds the return value
```

Two instructions. `lea` ("load effective address") is abused here as a fast add. The `rdi`-in, `eax`-out convention comes from the System V AMD64 ABI — the compiler and caller agree on which registers carry arguments and return values.

Reproduce it yourself:

```bash
gcc -S -masm=intel -O1 -o add_one.s add_one.c
cat add_one.s
```

Or disassemble an existing binary:

```bash
objdump -d -M intel ./my_program
```

## Why It Matters

Day-to-day application work almost never requires writing assembly, but reading it pays off in three situations:

- **Performance debugging** — when profiling shows a hot loop, `objdump` or Compiler Explorer (godbolt.org) reveals what the compiler actually emitted. Sometimes a one-line source change cuts the instruction count in half.
- **Reverse engineering and CTFs** — binaries ship as machine code. Assembly is the only view.
- **Low-level systems work** — kernels, bootloaders, codecs, crypto primitives, and [GPU](./04_gpu.md) kernels sometimes hand-write hot paths in assembly or intrinsics for guarantees the compiler can't provide.

For AWS work, assembly matters indirectly: switching an [EC2](../cloud/aws/compute/01_amazon_ec2.md) fleet from x86 to Graviton means every binary must be rebuilt for ARM64, because the machine code under the source is architecture-specific.

## Precautions

### MAIN PRECAUTION: Prefer Reading Over Writing

Hand-written assembly is rarely faster than modern optimizing compilers for general code, and it locks you to one architecture. Reach for intrinsics (C functions that map to specific instructions) before raw assembly when you need precise control.

### 1. Calling Conventions Differ

Which registers hold arguments, which are caller- vs callee-saved, and how the stack is aligned all depend on the ABI (System V on Linux/macOS, Microsoft x64 on Windows). Getting this wrong silently corrupts state.

### 2. Assembly Is Not Machine Code

The assembler still resolves labels, relocations, and encoding choices. Two syntactically different assembly lines can produce the same bytes; the same source line can encode differently depending on operand sizes.

### 3. Optimization Flags Change Output Drastically

`gcc -O0` and `gcc -O3` produce very different assembly. When inspecting compiler output, match the optimization level you ship.

---
↑ [Overview](./00_computing_overview.md)

**Related:** [Decomposition](09_decomposition.md), [CPU architecture](./01_architecture.md), [GPU](./04_gpu.md), [EC2](../cloud/aws/compute/01_amazon_ec2.md)
**Tags:** #computing
