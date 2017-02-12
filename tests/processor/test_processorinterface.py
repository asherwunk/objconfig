"""
Test objconfig.processor.ProcessorInterface
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.processor import ProcessorInterface


def test_methods_processorinterface():
    processor = ProcessorInterface()
    
    with pytest.raises(RuntimeException):
        processor.process('')
    with pytest.raises(RuntimeException):
        processor.processValue('')
