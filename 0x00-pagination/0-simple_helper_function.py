#!/usr/bin/env python3
"""funtion that takes two arguments and return A tuple"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    return start_index, end_index
