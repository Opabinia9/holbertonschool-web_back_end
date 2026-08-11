#!/usr/bin/env python3
"""Module: index_range."""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Get range of results on page <page> if each page is <page_size>.

    Returns:
        tuple of ints, lower and upper bounds for page <page>.

    """
    return (page_size * (page - 1)), page_size * page
