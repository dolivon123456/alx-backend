#!/usr/bin/env python3
"""
This module defines the function index_range
"""

def index_range(page: int, page_size: int) -> tuple:
    """ return a tuple of size two containing a start and end index """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
