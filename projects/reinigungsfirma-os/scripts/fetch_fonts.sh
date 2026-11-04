#!/usr/bin/env bash
# Downloads the self-hosted font files (OFL licensed) from npm @fontsource packages
# into site/fonts/. Run once after cloning, or whenever site/fonts/ is empty.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cd "$TMP"
npm pack @fontsource/schibsted-grotesk @fontsource/jetbrains-mono --silent >/dev/null
for f in *.tgz; do mkdir -p "${f%.tgz}"; tar xzf "$f" -C "${f%.tgz}"; done
mkdir -p "$ROOT/site/fonts"
for w in 400 500 600 700 800; do
  cp fontsource-schibsted-grotesk-*/package/files/schibsted-grotesk-latin-$w-normal.woff2 "$ROOT/site/fonts/"
done
for w in 400 500 600; do
  cp fontsource-jetbrains-mono-*/package/files/jetbrains-mono-latin-$w-normal.woff2 "$ROOT/site/fonts/"
done
ls "$ROOT/site/fonts"
