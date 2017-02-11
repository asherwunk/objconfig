"""
Test objconfig.reader.Xml
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.reader import Xml
import os


def test_emptyinstantiation_xml():
    conf = Xml()
    assert isinstance(conf, Xml), "Empty Instantiation Failed"

def test_readfromfile_xml():
    conf = Xml()
    config = conf.fromFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.xml"))
    assert config['database']['params']['dbname'] == 'dbproduction', "Reading test.xml File Failed"
    assert config['webhost'] == 'www.example.com', "Reading test.xml File Failed (xi)"

def test_readfromfile_nonexistent_xml():
    conf = Xml()
    with pytest.raises(RuntimeException):
        config = conf.fromFile("doesntexist.xml")

def test_readfromstring_xml():
    # IMPORTANT: Make sure strings begin right away with <?xml ...
    xmlstring = """<?xml version="1.0" encoding="utf-8"?>
<config xmlns:xi="http://www.w3.org/2001/XInclude">
    <webhost value="www.example.com"></webhost>
    <database>
        <adapter>pdo_mysql</adapter>
        <params>
            <host>db.example.com</host>
            <username>dbuser</username>
            <password>secret</password>
            <dbname>dbproduction</dbname>
        </params>
    </database>
</config>
"""
    conf = Xml()
    config = conf.fromString(xmlstring)
    assert config['database']['params']['dbname'] == 'dbproduction', "Reading XML String Failed"
    assert config['webhost'] == 'www.example.com', "Reading XML String Failed"

def test_readfromstring_improperinclude_xml():
    # IMPORTANT: Make sure strings begin right away with <?xml ...
    xmlstring = """<?xml version="1.0" encoding="utf-8"?>
<config xmlns:xi="http://www.w3.org/2001/XInclude">
    <webhost value="www.example.com"></webhost>
    <database>
        @include: another.xml
        <adapter>pdo_mysql</adapter>
        <params>
            <host>db.example.com</host>
            <username>dbuser</username>
            <password>secret</password>
            <dbname>dbproduction</dbname>
        </params>
    </database>
</config>
"""
    conf = Xml()
    with pytest.raises(RuntimeException):
        config = conf.fromString(xmlstring)
