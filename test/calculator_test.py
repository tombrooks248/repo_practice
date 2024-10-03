import pytest
from app.calculator import add_nums

def test_add():
    assert add_nums(5,7) == 12
