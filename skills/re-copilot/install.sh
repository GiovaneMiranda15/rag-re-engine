#!/usr/bin/env bash
# Instala a skill re-copilot no Claude Code (cópia em ~/.claude/skills/re-copilot).
# A skill é autocontida: o motor RAG opcional está em ./engine.
# Uso:
#   ./install.sh             # só a skill
#   ./install.sh --engine    # skill + motor RAG (comando rag-re-engine no PATH, via uv)
#   ./install.sh --force     # substitui uma cópia já instalada
# Variável: CLAUDE_SKILLS_DIR (default: ~/.claude/skills)
set -euo pipefail

ENGINE=0
FORCE=0
for arg in "$@"; do
  case "$arg" in
    --engine) ENGINE=1 ;;
    --force) FORCE=1 ;;
    *) echo "opção desconhecida: $arg" >&2; exit 2 ;;
  esac
done

SKILL_SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}/re-copilot"

copy_skill() {
  mkdir -p "$DEST"
  # Copia sem ambientes virtuais, índices e caches.
  (cd "$SKILL_SRC" && tar --exclude='.venv' --exclude='__pycache__' --exclude='*.db' \
      --exclude='.pytest_cache' --exclude='install.sh' -cf - .) | (cd "$DEST" && tar -xf -)
  echo "Skill copiada para $DEST"
}

if [ -L "$DEST" ] && [ "$(readlink -f "$DEST")" = "$SKILL_SRC" ]; then
  echo "Skill já instalada como symlink para $SKILL_SRC."
elif [ -e "$DEST" ]; then
  if [ "$FORCE" = 1 ]; then
    rm -rf "$DEST"
    copy_skill
  else
    echo "Skill já existe em $DEST (use --force para substituir)."
  fi
else
  copy_skill
fi

if [ "$ENGINE" = 1 ]; then
  command -v uv >/dev/null 2>&1 || { echo "uv não encontrado: https://docs.astral.sh/uv/" >&2; exit 1; }
  uv tool install --force "$SKILL_SRC/engine[embeddings]"
  echo "Motor instalado. Confira com: rag-re-engine --help"
fi
