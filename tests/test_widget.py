# tests/test_widget.py

import pytest
from src.widget import Widget


def test_widget_creation():
    widget = Widget(name="Test Widget", value=100)
    assert widget.name == "Test Widget"
    assert widget.value == 100


def test_add_transaction():
    widget = Widget(name="Test Widget", value=100)
    widget.add_transaction(50)
    assert widget.value == 150
    assert widget.transactions == [50]


def test_widget_display():
    widget = Widget(name="Test Widget", value=100)
    assert widget.display() == "Widget Test Widget: 100"
