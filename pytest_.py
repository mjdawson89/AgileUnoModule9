"""
Matthew Dawson
11/23/20
Module 9: Testing using Pytest
"""
#import pytest
import my_module


def test_greeting_pass():
    """
    Testing greeting function from my_module for pass
    """
    assert my_module.greeting("Matt") == "Hello Matt" , "test failed"

def test_greeting_fail():
    """
    Testing greeting function from my_module for fail
    """
    assert my_module.greeting("") != "Hello Matt", "test failed"

def test_letter_text_pass():
    """
    Testing letter_text function from my_module for pass
    """
    assert my_module.letter_text(name="Matt", amount="100", denomination="USD") == \
        "Hello Matt, this letter is to inform you that you have won 100 USD.", "test failed"

def test_letter_text_fail():
    """
    Testing letter_text function from my_module for fail
    """
    assert my_module.letter_text(name="Matt", amount="100") != \
        "Hello Matt, this letter is to inform you that you have won 100 USD.", "test failed"
