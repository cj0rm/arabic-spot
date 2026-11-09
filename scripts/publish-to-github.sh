#!/usr/bin/env bash
set -euo pipefail

REPO="cj0rm/arabic-spot"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! command -v git >/dev/null 2>&1; then
  echo "Install Git first: https://git-scm.com/downloads" >&2
  exit 1
fi
if ! command -v gh >/dev/null 2>&1; then
  echo "Install GitHub CLI first: https://cli.github.com/" >&2
  exit 1
fi
gh auth status >/dev/null || { echo "Run: gh auth login" >&2; exit 1; }
python3 scripts/validate.py

if [ ! -d .git ]; then
  git init -b main
fi
git add .
if ! git diff --staged --quiet; then
  git commit -m "feat: publish Arabic spot"
fi
if ! git remote get-url origin >/dev/null 2>&1; then
  git remote add origin "https://github.com/$REPO.git"
fi
git push -u origin main
echo "Published: https://github.com/$REPO"
