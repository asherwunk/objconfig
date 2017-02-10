"""
Test objconfig.util.ArrayAccess
"""

import pytest
from objconfig.exception import IndexException
from objconfig.util import ArrayAccess


def test_itemmethods_arrayaccess():
    access = ArrayAccess()
    
    with pytest.raises(IndexException):
        a = access[0]
    with pytest.raises(IndexException):
        access[0] = 1
    with pytest.raises(IndexException):
        del access[0]
