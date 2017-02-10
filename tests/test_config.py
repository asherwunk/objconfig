"""
Test objconfig.Config
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.exception import InvalidArgumentException
from objconfig import Config

def test_empty_instantiation():
    try:
        config = Config({})
    except Exception:
        assert False, "Empty Dictionary Instantiation Failed"

def test_normal_instantiation():
    try:
        config = Config({'spam': 'eggs'})
    except Exception:
        assert False, "Dictionary Instantiation Failed"

def test_with_config_instantiation():
    try:
        embed = Config({'spam': 'eggs'})
        config = Config({'brian': embed})
    except Exception:
        assert False, "Instantiation With Config Failed"
    assert config.brian.spam == 'eggs', "Instantiation With Config Failed"

def test_improper_instantiation():
    with pytest.raises(InvalidArgumentException):
        config = Config(['not', 'a', 'dictionary'])

def test_copy_config():
    l = [1,2,3,4,5]
    firstconfig = Config({'l': l})
    secondconfig = firstconfig.copy()
    l[0] = 6
    assert secondconfig.l[0] == 1, "Config Not Deep Copied"

def test_setattr_getattr_config():
    config = Config({}, allowModifications=True)
    config.spam = 'eggs'
    assert config.spam == 'eggs', "Config __setattr__/__getattr__ Not Working"

def test_len_config():
    config = Config({'life': 'brian', 'spam': 'eggs'})
    assert len(config) == 2, "Config __len__ Not Working"

def test_iter_config():
    testagainst = {}
    config = Config({'life': 'brian', 'spam': 'eggs'})
    for key, value in config:
        testagainst[key] = value
    assert {'life': 'brian', 'spam': 'eggs'} == testagainst, "Config __iter__ Not Working"

def test_itemmethods_config():
    config = Config({'life': 'brian', 'spam': {'ham': 'rabbit'}}, allowModifications=True)
    assert config['life'] == 'brian', "Config __getitem__ Not Working"
    config['spam']['ham'] = 'eggs'
    assert config['spam']['ham'] == 'eggs', "Config __setitem__ Not Working"
    del config['life']
    assert {'spam': {'ham': 'eggs'}} == config.toArray(), "Config __delitem__ Not Working"
    
    config.setReadOnly()
    with pytest.raises(RuntimeException):
        config['spam']['ham'] = 'foo'
    with pytest.raises(InvalidArgumentException):
        del config['spam']

def test_toArray_config():
    config = Config({'life': 'brian', 'spam': {'ham': 'rabbit'}})
    assert {'life': 'brian', 'spam': {'ham': 'rabbit'}} == config.toArray(), "Config toArray Not Working"

def test_isReadOnly_config():
    config = Config({'life': 'brian', 'spam': {'ham': 'rabbit'}})
    assert config.isReadOnly(), "Config isReadOnly Not Working"

def test_merge_config():
    config = Config({'life': 'brian', 'spam': {'ham': 'rabbit'}})
    merge = Config({'life': 'meaning', 'spam': {'ham': 'killer', 'new': 'ni'}})
    config.merge(merge)
    assert isinstance(config.spam, Config), "Config merge Not Working"
    assert {'life': 'meaning', 'spam': {'ham': 'killer', 'new': 'ni'}} == config.toArray(), "Config merge Not Working"
