#!/usr/bin/env python3
"""Module: ."""

import csv
import math
from os import preadv
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page <page> of size <page_size>.

        Returns:
            list of results between
            <page * (page_size - 1)> and <page * page_size>

        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get dataset metadata about the current page.

        Returns:
            page_size, page,
            data, next_page,
            prev_page, total_pages,

        """
        cur_page = self.get_page(page, page_size)
        prev_page = self.get_page(page, page_size)
        next_page = self.get_page(page, page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": cur_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": len(self.dataset()),
        }


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Get range of results on page <page> if each page is <page_size>.

    Returns:
        tuple of ints, lower and upper bounds for page <page>.

    """
    return (page_size * (page - 1)), page_size * page
