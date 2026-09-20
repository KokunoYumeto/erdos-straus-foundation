#!/usr/bin/env bash
# Run inside an authenticated clean clone of the intended repository.
set -euo pipefail
here="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo="KokunoYumeto/erdos-straus-foundation"
branch="research/es-turn07-fabel-bridge-20260920"
command -v gh >/dev/null
[[ -z "$(git status --porcelain)" ]] || { echo 'A clean working tree is required.' >&2; exit 1; }
gh auth status >/dev/null
remote="$(git remote get-url origin)"
case "$remote" in *KokunoYumeto/erdos-straus-foundation*) ;; *) echo 'Unexpected repository origin.' >&2; exit 1;; esac
git fetch origin main
git switch -c "$branch" origin/main
git apply --check "$here/integration.patch"
git apply "$here/integration.patch"
git add research/incoming/es-turn07-fabel-bridge-20260920
git commit -m 'research(es): original-prime Fabel fibres and negative-square channel returns'
git push -u origin "$branch"
gh pr create --repo "$repo" --base main --head "$branch" --draft \
 --title 'ES: prime-local Fabel fibres and same-prime channel returns' \
 --body-file "$here/PR_BODY.md"
