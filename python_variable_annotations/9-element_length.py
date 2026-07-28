#!/usr/bin/env python3
"""Module: element_length."""

import typing


def element_length(
    lst: typing.Iterable[typing.Sequence],
) -> typing.List[typing.Tuple]:
    """Find the length of each element in a list.

    Returns:
        list of tuples

    """
    return [(i, len(i)) for i in lst]
