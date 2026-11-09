#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$HOME/.agents/skills/arabic-spot"
if [ -e "$TARGET" ]; then
  echo "Skill already exists at $TARGET. Remove or back it up before installing." >&2
  exit 1
fi
mkdir -p "$(dirname "$TARGET")"
cp -R "$ROOT" "$TARGET"
rm -rf "$TARGET/.git"
echo "Arabic spot installed at $TARGET"
echo 'In Codex, try: $arabic-spot اكتب قصيدة عن عُمان'
