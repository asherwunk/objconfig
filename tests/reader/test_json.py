"""
Test objconfig.util.ArrayAccess
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.reader import Json
import os


def test_emptyinstantiation_json():
    conf = Json()
    assert isinstance(conf, Json), "Empty Instantiation Failed"

def test_readfromfile_ini():
    conf = Json()
    config = conf.fromFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.json"))
    assert config['database']['adapter'] == 'pdo_mysql', "Reading test.ini File Failed"
    assert config['includedfile']['webhost'] == 'www.exampletwo.com', "Reading test.json File Failed (@include)"

def test_readfromstring_json():
    jsonstring = """
{
  "webhost"  : "www.example.com",
  "database" : {
    "adapter" : "pdo_mysql",
    "params"  : {
      "host"     : "db.example.com",
      "username" : "dbuser",
      "password" : "secret",
      "dbname"   : "dbproduction"
    }
  }
}
"""
    conf = Json()
    config = conf.fromString(jsonstring)
    assert config['database']['params']['host'] == 'db.example.com', "Reading test.json File Failed"

def test_readfromstring_improperinclude_json():
    jsonstring = """
{
  "webhost"  : "www.example.com",
  "database" : {
    "adapter" : "pdo_mysql",
    "params"  : {
      "host"     : "db.example.com",
      "username" : "dbuser",
      "password" : "secret",
      "dbname"   : "dbproduction"
    }
  },
  "includedfile" :
    "@include" : "another.json"
}
"""
    conf = Json()
    with pytest.raises(RuntimeException):
        config = conf.fromString(jsonstring)