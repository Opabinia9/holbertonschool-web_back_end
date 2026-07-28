#!/usr/bin/env python3
"""Module: make_multiplier."""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Make a function for multiplying by multiplier.

    Returns:
        Function that multipyes its paramater my multiplier.

    """
    return lambda x: x * multiplier
