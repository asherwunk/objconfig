"""
Test objconfig.util.ArrayAccess
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.util import Iterator


def test_itemmethods_iterator():
    i = Iterator()
    
    with pytest.raises(RuntimeException):
        for a in i:
            pass
