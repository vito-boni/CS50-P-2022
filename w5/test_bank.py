# (unit test) test_bank.py
from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('hello, babe') == 0

def test_h():
    assert value('hi') == 20
    assert value('how are you') == 20
    assert value('hallo freund') == 20
    assert value('hel lo') == 20

def test_saywhat():
    assert value('whats good') == 100
    assert value('what so ever') == 100

def test_capital():
    assert value('HELLO') == 0
    assert value('Hey') == 20
