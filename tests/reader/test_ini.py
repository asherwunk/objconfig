"""
Test objconfig.util.ArrayAccess
"""

import pytest
from objconfig.exception import RuntimeException
from objconfig.reader import Ini
import os


def test_emptyinstantiation_ini():
    ini = Ini()
    assert ini.getNestSeparator() == '.', "Empty Instantiation Failed"

def test_readfromfile_ini():
    ini = Ini()
    config = ini.fromFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.ini"))
    assert config['database']['port'] == '143', "Reading test.ini File Failed"
    assert config['database']['server']['ipaddress'] == '192.0.2.62', "Reading test.ini File Failed"
    assert config['website']['server']['ipaddress'] == '192.0.3.128', "Reading test.ini File Failed (@include)"

def test_readfromstring_ini():
    inistring = """
; last modified 1 April 2001 by John Doe
[owner]
name=John Doe
organization=Acme Widgets Inc.

[database]
; use IP address in case network name resolution is not working
server.ipaddress=192.0.2.62
port=143
file="payroll.dat"
"""
    ini = Ini()
    config = ini.fromString(inistring)
    assert config['database']['port'] == '143', "Reading test.ini File Failed"
    assert config['database']['server']['ipaddress'] == '192.0.2.62', "Reading test.ini File Failed"

def test_readfromstring_impropersubkey_ini():
    inistring = """
; last modified 1 April 2001 by John Doe
[owner]
name=John Doe
organization=Acme Widgets Inc.

[database]
; use IP address in case network name resolution is not working
server.ipaddress=192.0.2.62
server.ipaddress.mask=0.0.0.1
port=143
file="payroll.dat"
"""
    ini = Ini()
    with pytest.raises(RuntimeException):
        config = ini.fromString(inistring)

def test_readfromstring_improperinclude_ini():
    inistring = """
; last modified 1 April 2001 by John Doe
[owner]
name=John Doe
organization=Acme Widgets Inc.

[database]
; use IP address in case network name resolution is not working
server.ipaddress=192.0.2.62
port=143
file="payroll.dat"

@include=another.ini
"""
    ini = Ini()
    with pytest.raises(RuntimeException):
        config = ini.fromString(inistring)

def test_readfromstring_nestedsections_ini():
    inistring = """
; last modified 1 April 2001 by John Doe
[owner.profile]
name=John Doe
organization=Acme Widgets Inc.

[owner.position]
job=manager

[database]
; use IP address in case network name resolution is not working
server.ipaddress=192.0.2.62
port=143
file="payroll.dat"
"""
    ini = Ini()
    config = ini.fromString(inistring)
    assert config['owner']['profile']['name'] == 'John Doe', "Reading test.ini File Failed"
    assert config['owner']['position']['job'] == 'manager', "Reading test.ini File Failed"
