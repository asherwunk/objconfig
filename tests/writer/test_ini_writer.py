"""
Test objconfig.writer.Ini
"""

from objconfig.writer import Ini as IniWriter
from objconfig.reader import Ini as IniReader
from objconfig.writer import AbstractWriter
from objconfig.writer import WriterInterface
import os


def test_emptyinstantiation_ini():
    writer = IniWriter()
    assert isinstance(writer, AbstractWriter), "Ini not child of AbstractWriter"
    assert isinstance(writer, WriterInterface), "Ini not child of WriterInterface"

def test_renderwithsections_ini():
    writer = IniWriter()
    conf = {"owner": {"name": "John Doe", "organization": "Acme Widgets Inc."},
            "database": {"server": {"ipaddress": "192.0.2.62"}, "port": "143", "file": "payroll.dat"}}
    inicontents = writer.toString(conf)
    reader = IniReader()
    compconf = reader.fromString(inicontents)
    if not compconf["DEFAULT"]:
        del compconf["DEFAULT"]
    assert conf == compconf, "Ini improperly rendered with sections"

def test_renderwithoutsections_ini():
    writer = IniWriter(renderWithoutSections=True)
    conf = {"owner": {"name": "John Doe", "organization": "Acme Widgets Inc."},
            "database": {"server": {"ipaddress": "192.0.2.62"}, "port": "143", "file": "payroll.dat"}}
    inicontents = writer.toString(conf)
    reader = IniReader()
    compconf = reader.fromString(inicontents)
    compconf.update(compconf["DEFAULT"])
    del compconf["DEFAULT"]
    assert conf == compconf, "Ini improperly rendered without sections"

def test_renderwithsections_tofile_ini():
    writer = IniWriter()
    conf = {"owner": {"name": "John Doe", "organization": "Acme Widgets Inc."},
            "database": {"server": {"ipaddress": "192.0.2.62"}, "port": "143", "file": "payroll.dat"}}
    writer.toFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.ini"), conf)
    reader = IniReader()
    compconf = reader.fromFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.ini"))
    if not compconf["DEFAULT"]:
        del compconf["DEFAULT"]
    assert conf == compconf, "Ini improperly rendered with sections in file"
    os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.ini"))

def test_renderwithoutsections_tofile_ini():
    writer = IniWriter(renderWithoutSections=True)
    conf = {"owner": {"name": "John Doe", "organization": "Acme Widgets Inc."},
            "database": {"server": {"ipaddress": "192.0.2.62"}, "port": "143", "file": "payroll.dat"}}
    writer.toFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.ini"), conf)
    reader = IniReader()
    compconf = reader.fromFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.ini"))
    compconf.update(compconf["DEFAULT"])
    del compconf["DEFAULT"]
    assert conf == compconf, "Ini improperly rendered without sections"
    os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.ini"))
