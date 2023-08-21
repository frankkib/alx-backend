#!/usr/bin/env python3
"""funtion that takes two arguments and return A tuple"""
from typing import List
import csv
import math


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    return start_index, end_index


class Server:
    """server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """class initializer"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns the dataset of the page"""
        assert isinstance(page, int) and page > 0, "Invalid page argument"
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index+1]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """function that returns a dictionary of popular baby names"""
        total_pages = math.ceil(len(self.dataset()) / page_size)
        start_index, end_index = index_range(page, page_size)
        hyper_data = {
                'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': page + 1 if page  < total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
                }
        return hyper_data
