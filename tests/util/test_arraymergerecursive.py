"""
Test objconfig.util.array_merge_recursive
"""

import pytest
from objconfig.util import array_merge_recursive


def test_arraymergerecursive():
    array1 = {'a': 1, 'b': 2}
    array2 = {'b': 3, 'c': 4}
    ret = array_merge_recursive(array1, array2)
    assert ret == {'b': 3, 'a': 1, 'c': 4}, "array_merge_recursive Failed"
    