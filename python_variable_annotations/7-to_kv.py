#!/usr/bin/env python3
"""Module: to_kv."""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> tuple:
    """Return tuple of k and (v squred).

    Returns:
        tuple of k, and v**2.

    """
    value: float = v**2
    return k, value
