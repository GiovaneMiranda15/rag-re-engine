#!/usr/bin/env bash
# Instala a skill re-copilot no Claude Code (cópia em ~/.claude/skills/re-copilot).
# Uso:
#   ./install.sh                      # só a skill
#   ./install.sh --engine <repo>      # skill + rag-re-engine a partir de um clone do repositório
set -euo pipefail

SKILL_SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}/re-copilot"

if [ -e "$DEST" ] || [ -L "$DEST" ]; then
  if [ "$(readlink -f "$DEST")" = "$SKILL_SRC" ]; then
    echo "Skill já instalada (aponta para $SKILL_SRC)."
  else
    echo "Já existe $DEST. Remova ou mova antes de reinstalar." >&2
    exit 1
  fi
else
  mkdir -p "$(dirname "$DEST")"
  cp -r "$SKILL_SRC" "$DEST"
  rm -f "$DEST/install.sh"
  echo "Skill copiada para $DEST"
fi

if [ "${1:-}" = "--engine" ]; then
  REPO="${2:?informe o caminho do clone do repositório (que contém rag-re-engine/)}"
  command -v uv >/dev/null 2>&1 || { echo "uv não encontrado: https://docs.astral.sh/uv/" >&2; exit 1; }
  uv tool install --force "$REPO/rag-re-engine[embeddings]"
  echo "rag-re-engine instalado. Confira com: rag-re-engine --help"
fi
