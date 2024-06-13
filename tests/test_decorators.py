import pytest
import logging
from src.decorators import log

@log()
def add(x, y):
    return x + y

@log()
def raise_exception(x, y):
    raise ValueError("An error occurred")

def test_add(caplog):
    result = add(3, 4)
    assert result == 7
    assert "add ok" in caplog.text

def test_raise_exception(caplog):
    with pytest.raises(ValueError, match="An error occurred"):
        raise_exception(1, 2)
    assert "raise_exception error: ValueError. Inputs: (1, 2), {}" in caplog.text
