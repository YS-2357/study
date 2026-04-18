#!/usr/bin/env bash
# Git credential helper: reads GITHUB_USERNAME and GITHUB_TOKEN from .env.
# Registered via: git config --local credential.helper
# so that plain `git push` works without a special command.

ROOT="$(git rev-parse --show-toplevel)"
ENV_FILE="$ROOT/.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "error: $ENV_FILE not found" >&2
  exit 1
fi

read_env_value() {
  local key="$1"
  local line value

  line="$(grep -m1 -E "^[[:space:]]*(export[[:space:]]+)?${key}=" "$ENV_FILE" || true)"
  value="${line#*=}"
  value="${value%$'\r'}"

  case "$value" in
    \"*\") value="${value#\"}"; value="${value%\"}" ;;
    \'*\') value="${value#\'}"; value="${value%\'}" ;;
  esac

  printf '%s' "$value"
}

GITHUB_TOKEN="$(read_env_value GITHUB_TOKEN)"
GITHUB_USERNAME="$(read_env_value GITHUB_USERNAME)"

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "error: GITHUB_TOKEN not set in $ENV_FILE" >&2
  exit 1
fi

if [[ -z "${GITHUB_USERNAME:-}" ]]; then
  echo "error: GITHUB_USERNAME not set in $ENV_FILE" >&2
  exit 1
fi

echo "username=$GITHUB_USERNAME"
echo "password=$GITHUB_TOKEN"
