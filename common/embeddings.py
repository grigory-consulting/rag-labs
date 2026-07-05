"""Lokale Embeddings für die RAG-Komplettkurs-Labs.

Nutzt sentence-transformers, läuft also unabhängig vom LLM-Backend immer lokal.
Das Default-Modell ist mehrsprachig und passt zu den deutschen Beispieldokumenten.

Umgebungsvariablen:
  LAB_EMBED_MODEL   Default "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
"""
from __future__ import annotations

import os
from functools import lru_cache

import numpy as np

EMBED_MODEL = os.environ.get(
    "LAB_EMBED_MODEL",
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
)


@lru_cache(maxsize=2)
def _model(name: str):
    from sentence_transformers import SentenceTransformer  # lazy import

    return SentenceTransformer(name)


def embed(texts, model: str | None = None, normalize: bool = True) -> np.ndarray:
    """Embedde eine Liste von Strings zu einer (n, d)-Matrix.

    normalize=True liefert L2-normierte Vektoren, sodass das Skalarprodukt
    direkt die Cosine-Similarity ist (siehe Teil V der Folien).
    """
    if isinstance(texts, str):
        texts = [texts]
    vecs = _model(model or EMBED_MODEL).encode(
        list(texts), normalize_embeddings=normalize, show_progress_bar=False
    )
    return np.asarray(vecs, dtype=np.float32)


def cosine(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Cosine-Similarity zwischen Zeilen von a und Zeilen von b -> (len(a), len(b))."""
    a = np.atleast_2d(a)
    b = np.atleast_2d(b)
    an = a / (np.linalg.norm(a, axis=1, keepdims=True) + 1e-12)
    bn = b / (np.linalg.norm(b, axis=1, keepdims=True) + 1e-12)
    return an @ bn.T


def active_model() -> str:
    return EMBED_MODEL
