"""Backends de LLM usados pelos avaliadores dos pipelines (ex.: retrieval evaluator do CRAG).

O motor depende só do protocolo `LLM`; o backend concreto é escolhido na CLI.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from typing import Protocol


class LLM(Protocol):
    name: str

    def complete(self, prompt: str) -> str: ...


class ClaudeCliLLM:
    """Usa o Claude Code em modo headless (`claude -p`), sem ferramentas. Não exige API key."""

    def __init__(self, model: str | None = None, timeout_s: int = 180) -> None:
        self.model = model
        self.timeout_s = timeout_s
        self.name = f"claude-cli:{model or 'default'}"

    def complete(self, prompt: str) -> str:
        argv = ["claude", "-p", "--output-format", "json", "--no-session-persistence", "--permission-mode", "dontAsk"]
        if self.model:
            argv += ["--model", self.model]
        env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
        result = subprocess.run(argv, input=prompt, capture_output=True, text=True, timeout=self.timeout_s, env=env)
        if result.returncode != 0:
            raise RuntimeError(f"claude -p falhou (exit {result.returncode}): {result.stderr.strip()[:300]}")
        payload = json.loads(result.stdout)
        if payload.get("is_error"):
            raise RuntimeError(f"claude -p retornou erro: {str(payload.get('result'))[:300]}")
        return payload.get("result", "")


def get_llm(spec: str) -> LLM:
    """`claude` ou `claude:<modelo>`."""
    kind, _, arg = spec.partition(":")
    if kind == "claude":
        return ClaudeCliLLM(model=arg or None)
    raise ValueError(f"LLM desconhecido: {spec}")


def parse_json(text: str) -> dict | list:
    """Extrai o primeiro objeto/array JSON de uma resposta de LLM (tolera texto e cercas ```)."""
    fence = re.search(r"```(?:json)?\s*([\[{].*[\]}])\s*```", text, re.S)
    candidates = [fence.group(1)] if fence else []
    for opener, closer in (("{", "}"), ("[", "]")):
        start, end = text.find(opener), text.rfind(closer)
        if start != -1 and end > start:
            candidates.append(text[start : end + 1])
    for candidate in candidates:
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            continue
    raise ValueError(f"resposta sem JSON válido: {text[:200]}")
