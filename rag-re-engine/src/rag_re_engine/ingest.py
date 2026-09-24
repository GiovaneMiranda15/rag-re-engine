"""Leitura do corpus (txt, md, pdf) e divisão determinística em chunks."""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

from rag_re_engine.models import Chunk

SUPPORTED_SUFFIXES = {".txt", ".md", ".pdf"}


def load_documents(root: Path) -> dict[str, str]:
    """Retorna {doc_id: texto}. doc_id é o caminho relativo a `root`."""
    root = Path(root)
    docs: dict[str, str] = {}
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED_SUFFIXES):
        text = _read_pdf(path) if path.suffix.lower() == ".pdf" else path.read_text(errors="replace")
        if text.strip():
            docs[str(path.relative_to(root))] = text
    return docs


def _read_pdf(path: Path) -> str:
    # pdftotext (poppler-utils) evita uma dependência Python só para extração de texto.
    if not shutil.which("pdftotext"):
        raise RuntimeError("pdftotext não encontrado; instale poppler-utils para indexar PDFs.")
    result = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"falha ao extrair texto de {path}: {result.stderr.strip()[:200]}")
    return result.stdout


def chunk_text(doc_id: str, text: str, max_chars: int = 1200, overlap: int = 200) -> list[Chunk]:
    """Agrupa parágrafos até `max_chars`; parágrafos maiores são cortados com sobreposição."""
    paragraphs = [" ".join(p.split()) for p in re.split(r"\n\s*\n", text)]
    pieces: list[str] = []
    for paragraph in filter(None, paragraphs):
        if len(paragraph) <= max_chars:
            pieces.append(paragraph)
            continue
        step = max_chars - overlap
        pieces.extend(paragraph[i : i + max_chars] for i in range(0, len(paragraph), step))

    chunks: list[str] = []
    current = ""
    for piece in pieces:
        if current and len(current) + 1 + len(piece) > max_chars:
            chunks.append(current)
            current = piece
        else:
            current = f"{current} {piece}".strip()
    if current:
        chunks.append(current)

    return [Chunk(chunk_id=f"{doc_id}#{i}", doc_id=doc_id, position=i, text=c) for i, c in enumerate(chunks)]


def split_strips(text: str, sentences_per_strip: int = 2) -> list[str]:
    """Divide um chunk em "knowledge strips" (grupos de sentenças), como no refinamento do CRAG."""
    sentences = [s.strip() for s in re.split(r"(?<=[.!?;])\s+", text) if s.strip()]
    return [" ".join(sentences[i : i + sentences_per_strip]) for i in range(0, len(sentences), sentences_per_strip)]
