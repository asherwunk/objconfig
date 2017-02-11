"""
Test objconfig.reader.Yaml
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.reader import Yaml
import os


def test_emptyinstantiation_json():
    conf = Yaml()
    assert isinstance(conf, Yaml), "Empty Instantiation Failed"

def test_readfromfile_json():
    conf = Yaml()
    config = conf.fromFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.yaml"))
    assert config['webhost']['server'] == 'www.example.com', "Reading test.yaml File Failed"
    assert config['database']['params']['host'] == 'db.example.com', "Reading test.yaml File Failed (@include)"

def test_readfromfile_nonexistent_yaml():
    conf = Yaml()
    with pytest.raises(RuntimeException):
        config = conf.fromFile("doesntexist.yaml")

def test_readfromstring_yaml():
    yamlstring = """
webhost:
    server: www.example.com
database:
    adapter: pdo_mysql
    params:
      host:     db.example.com
      username: dbuser
      password: secret
      dbname:   dbproduction
"""
    conf = Yaml()
    config = conf.fromString(yamlstring)
    assert config['database']['params']['host'] == 'db.example.com', "Reading YAML String Failed"

def test_readfromstring_improperinclude_yaml():
    yamlstring = """
webhost:
    server: www.example.com
    _@include: error.yaml
database:
    adapter: pdo_mysql
    params:
      host:     db.example.com
      username: dbuser
      password: secret
      dbname:   dbproduction
"""
    conf = Yaml()
    with pytest.raises(RuntimeException):
        config = conf.fromString(yamlstring)

