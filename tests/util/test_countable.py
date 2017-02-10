"""
Test objconfig.util.ArrayAccess
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.util import Countable


def test_itemmethods_countable():
    count = Countable()
    
    with pytest.raises(RuntimeException):
        len(count)
