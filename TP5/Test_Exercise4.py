import pytest
from funciones_exercise4 import *

@pytest.mark.parametrize("num1, num2, res",[
    (8,2,0),
    (16,8,0),
    (150,5,0),
    (28,7,0),
    (30,10,0),

])
def test_check(num1, num2, res):
    assert check (num1, num2) == res