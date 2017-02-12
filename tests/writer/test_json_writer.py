"""
Test objconfig.writer.Ini
"""

from objconfig.writer import Json as JsonWriter
from objconfig.reader import Json as JsonReader
from objconfig.writer import AbstractWriter
from objconfig.writer import WriterInterface
import os


def test_emptyinstantiation_json():
    writer = JsonWriter()
    assert isinstance(writer, AbstractWriter), "Ini not child of AbstractWriter"
    assert isinstance(writer, WriterInterface), "Ini not child of WriterInterface"

def test_render_json():
    writer = JsonWriter()
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
    
    jsoncontents = writer.toString(conf)
    reader = JsonReader()
    compconf = reader.fromString(jsoncontents)
    assert conf == compconf, "Json improperly rendered"

def test_render_tofile_json():
    writer = JsonWriter()
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
    writer.toFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.json"), conf)
    reader = JsonReader()
    compconf = reader.fromFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.json"))
    os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.json"))
    assert conf == compconf, "Json improperly rendered in file"
