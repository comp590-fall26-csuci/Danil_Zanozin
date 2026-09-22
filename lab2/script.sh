#!/usr/bin/env bash
set -euo pipefail

file="passwords.txt"

sort "$file" | while IFS= read -r password; do
	[[ -z "$password" ]] && continue
	echo "$password"
	printf '%s\n' "$password" > "$password"
done
