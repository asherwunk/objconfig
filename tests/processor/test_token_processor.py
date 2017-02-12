"""
Test objconfig.reader.Xml
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.processor import ProcessorInterface
from objconfig.processor import Token
from objconfig import Config


def test_emptyinstantiation_token():
    token = Token({})
    assert isinstance(token, ProcessorInterface), "Token not child of ProcessorInterface"

def test_replacewithdictionary_token():
    conf = {
      "webhost"  : "WEBHOST",
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
    
    token = Token({"WEBHOST": "www.example.com"})
    assert conf["webhost"] == "WEBHOST", "Failed conf building"
    conf = token.process(conf)
    assert conf["webhost"] == "www.example.com", "Failed conf token replacement"

def test_replacewithconfig_token():
    conf = {
      "webhost"  : "www.example.com",
      "database" : {
        "adapter" : "DBADAPTER",
        "params"  : {
          "host"     : "DBHOST",
          "username" : "dbuser",
          "password" : "secret",
          "dbname"   : "dbproduction"
        }
      }
    }
    
    config = Config(conf, True)
    token = Token({"DBHOST": "db.example.com", "DBADAPTER": "pdo_mysql"})
    assert config.database.params.host == "DBHOST", "Failed Config construction"
    assert config.database.adapter == "DBADAPTER", "Failed Config construction"
    config = token.process(config)
    assert config.database.params.host == "db.example.com", "Failed Config token replacement"
    assert config.database.adapter == "pdo_mysql", "Failed Config token replacement"

def test_replacewithdictionary_prefixandsuffix_token():
    conf = {
      "webhost"  : "__WEBHOST__",
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
    
    token = Token({"WEBHOST": "www.example.com"}, "__", "__")
    assert conf["webhost"] == "__WEBHOST__", "Failed conf building"
    conf = token.process(conf)
    assert conf["webhost"] == "www.example.com", "Failed conf token replacement"

def test_replacewithdictionary_addtoken_token():
    conf = {
      "webhost"  : "WEBHOST",
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
    
    token = Token({})
    token.addToken("WEBHOST", "www.example.com")
    assert conf["webhost"] == "WEBHOST", "Failed conf building"
    conf = token.process(conf)
    assert conf["webhost"] == "www.example.com", "Failed conf token replacement"

def test_replacewithdictionary_processvalue_token():
    conf = {
      "webhost"  : "WEBHOST",
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
    
    token = Token({"WEBHOST": "www.example.com"})
    assert conf["webhost"] == "WEBHOST", "Failed conf building"
    conf["webhost"] = token.processValue(conf["webhost"])
    assert conf["webhost"] == "www.example.com", "Failed conf token replacement"
