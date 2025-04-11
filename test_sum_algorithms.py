"""
Tests for the sum_algorithms module.
"""

from lib.sum_algorithms import sum_list, sum_list_nested

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0
    assert sum_list([-1, 1]) == 0

def test_sum_list_nested():
    assert sum_list_nested([1, 2, 3]) == 6
    assert sum_list_nested([]) == 0
    assert sum_list_nested([-1, 1]) == 0
