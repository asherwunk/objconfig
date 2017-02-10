"""
Test objconfig.util.ArrayAccess
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.reader import ReaderInterface


def test_methods_readerinterface():
    reader = ReaderInterface()
    
    with pytest.raises(RuntimeException):
        reader.fromFile('')
    with pytest.raises(RuntimeException):
        reader.fromString('')

