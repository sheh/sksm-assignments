import pytest

from text import Text

def test_process():
    text = Text("hello")
    assert text.process().t == "HELLO"

def test_trim():
    text = Text("  hello  ")
    assert text.trim().t == "hello"

def test_reverse():
    text = Text("hello")
    assert text.reverse().t == "olleh"
    
def test_length():
    text = Text("hello")
    assert text.length() == 5
    
def test_add():
    text1 = Text("hello")
    text2 = Text("world")
    assert text1 + text2 == Text("helloworld")
    
def test_to_lower():
    text = Text("HELLO")
    assert text.to_lower().t == "hello"

def test_to_upper():
    text = Text("hello")
    assert text.to_upper().t == "HELLO"
    
def test_to_capitalize():
    text = Text("hello")
    assert text.to_capitalize().t == "Hello"
    
def test_split():
    text = Text("hello,world")
    assert text.split(",") == [Text("hello"), Text("world")]
    
def test_eq():
    text1 = Text("hello")
    text2 = Text("hello")
    assert text1 == text2
