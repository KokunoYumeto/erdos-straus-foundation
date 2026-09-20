#!/usr/bin/env bash
# Run explicitly from an authenticated Git/gh environment. No force push.
set -euo pipefail
HERE=$(cd -- "$(dirname -- "$0")" && pwd)
if [[ $# -ne 1 ]]; then
  printf 'Usage: %s /path/to/clean/erdos-straus-foundation-clone\n' "$0" >&2
  exit 2
fi
REPO=$1
command -v git >/dev/null
command -v gh >/dev/null
cd -- "$REPO"
[[ -d .git ]] || { echo 'Expected a Git working clone.' >&2; exit 2; }
[[ -z $(git status --porcelain) ]] || { echo 'The working tree must be clean.' >&2; exit 2; }
case "$(git remote get-url origin)" in
  *KokunoYumeto/erdos-straus-foundation*) ;;
  *) echo 'Origin is not the specified foundation repository.' >&2; exit 2;;
esac
git fetch origin main
BRANCH=research/es-integral-completion-20260920
git checkout -b "$BRANCH" origin/main
git apply --check "$HERE/integration.patch"
git am "$HERE/integration.patch"
git push -u origin "$BRANCH"
gh pr create --repo KokunoYumeto/erdos-straus-foundation --base main \
  --head "$BRANCH" --draft \
  --title 'research(es): integral signed completion and source-domain obstruction' \
  --body-file "$HERE/PR_BODY.md"
