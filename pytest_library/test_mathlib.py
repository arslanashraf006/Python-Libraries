#write the file name and function name for testing starts with test, or you can also google to find more test dicovery role for pytest
# commamds to run
# python -m pytest
# py.test
# py.test -v //v means verbose shows the functions to be process

import mathlib

def test_cal_total():
    total = mathlib.cal_total(4,5)
    assert total == 9

def test_cal_multiply():
    result = mathlib.calc_multiply(10,3)
    assert result == 30