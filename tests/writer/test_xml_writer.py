"""
Test objconfig.writer.Xml
"""

from objconfig.writer import Xml as XmlWriter
from objconfig.reader import Xml as XmlReader
from objconfig.writer import AbstractWriter
from objconfig.writer import WriterInterface
import os


def test_emptyinstantiation_xml():
    writer = XmlWriter()
    assert isinstance(writer, AbstractWriter), "Xml not child of AbstractWriter"
    assert isinstance(writer, WriterInterface), "Xml not child of WriterInterface"

def test_render_xml():
    writer = XmlWriter()
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
    
    xmlcontents = writer.toString(conf)
    reader = XmlReader()
    compconf = reader.fromString(xmlcontents)
    assert conf == compconf, "Xml improperly rendered"

def test_render_tofile_xml():
    writer = XmlWriter()
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
    writer.toFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.xml"), conf)
    reader = XmlReader()
    compconf = reader.fromFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.xml"))
    os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.xml"))
    assert conf == compconf, "Xml improperly rendered in file"
