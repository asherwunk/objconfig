"""
Test objconfig.writer.Yaml
"""

from objconfig.writer import Yaml as YamlWriter
from objconfig.reader import Yaml as YamlReader
from objconfig.writer import AbstractWriter
from objconfig.writer import WriterInterface
import os


def test_emptyinstantiation_yaml():
    writer = YamlWriter()
    assert isinstance(writer, AbstractWriter), "Yaml not child of AbstractWriter"
    assert isinstance(writer, WriterInterface), "Yaml not child of WriterInterface"

def test_render_yaml():
    writer = YamlWriter()
    conf = {
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
    
    yamlcontents = writer.toString(conf)
    reader = YamlReader()
    compconf = reader.fromString(yamlcontents)
    assert conf == compconf, "Yaml improperly rendered"

def test_render_tofile_xml():
    writer = YamlWriter()
    conf = {
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
    writer.toFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.yaml"), conf)
    reader = YamlReader()
    compconf = reader.fromFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.yaml"))
    os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.yaml"))
    assert conf == compconf, "Yaml improperly rendered in file"
