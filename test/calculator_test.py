import pytest
from app.calculator import add_nums
from app.calculator import subtract_nums

def test_add():
    assert add_nums(5,7) == 12

def test_subtract():
    assert subtract_nums(10, 6) == 4
