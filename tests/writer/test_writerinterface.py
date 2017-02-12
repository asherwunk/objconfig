"""
Test objconfig.writer.WriterInterface
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.writer import WriterInterface


def test_methods_writerinterface():
    writer = WriterInterface()
    
    with pytest.raises(RuntimeException):
        writer.toFile('', None)
    with pytest.raises(RuntimeException):
        writer.toString(None)
