#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List[str]]:
        """Da Cached dataset.

        Returns:
            ...

        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset: list[list[str]] | None = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0.

        Returns:
            ...

        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """"""
        start, end = (
            (index),
            (index + page_size),
        )
        indexed_data: dict = self.indexed_dataset()
        assert indexed_data.get(start) is not None
        data = [
            indexed_data.get(x)
            for x in range(start, end)
            if indexed_data.get(x)
        ]
        return {
            "index": page_size * (index - 1 if index else 0),
            "next_index": page_size * (index if index else 1),
            "page_size": page_size,
            "data": data,
        }
