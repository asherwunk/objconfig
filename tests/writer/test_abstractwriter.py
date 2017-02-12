"""
Test objconfig.writer.AbstractWriter
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.writer import WriterInterface
from objconfig.writer import AbstractWriter
from objconfig import Config
import os


def test_methods_abstractwriter():
    writer = AbstractWriter()
    conf = Config({})
    
    assert isinstance(writer, WriterInterface), "AbstractWriter not instance of WriterInterface"
    
    with pytest.raises(RuntimeException):
        writer.toFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test"), conf)
    with pytest.raises(RuntimeException):
        writer.toString(conf)
    
    os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test"))
