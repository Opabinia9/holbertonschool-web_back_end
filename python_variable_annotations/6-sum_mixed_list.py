#!/usr/bin/env python3
"""Module: sum_mixed_list."""

import typing


def sum_mixed_list(mxd_lst: typing.List[int | float]) -> float:
    """Sum all elements from a list of ints and floats.

    Returns:
        Sum of all elements from list.

    """
    return sum(mxd_lst)
