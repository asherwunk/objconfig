"""
Test objconfig.Config
"""

from objconfig import Config

def test_empty_instantiation():
    try:
        config = Config({})
    except Exception:
        assert False, "Empty Dictionary Instantiation Failed"

def test_instantiation():
    try:
        config = Config({'spam': 'eggs'})
    except Exception:
        assert False, "Dictionary Instantiation Failed"
