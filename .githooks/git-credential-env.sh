#!/usr/bin/env bash
# Git credential helper — reads GITHUB_TOKEN from .env at repo root.
# Registered via: git config --local credential.helper
# so that plain `git push` works without a special command.

ROOT="$(git rev-parse --show-toplevel)"
ENV_FILE="$ROOT/.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "error: $ENV_FILE not found" >&2
  exit 1
fi

set -a && source "$ENV_FILE" && set +a

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "error: GITHUB_TOKEN not set in $ENV_FILE" >&2
  exit 1
fi

echo "username=YS-2357"
echo "password=$GITHUB_TOKEN"
