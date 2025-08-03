#write the file name and function name for testing starts with test, or you can also google to find more test dicovery role for pytest
# commamds to run
# python -m pytest
# pytest
# pytest -v //v means verbose shows the functions to be process
#if I dont want to use skip and run only specify function then I used k command
# pytest -k multiply -v --> it will run all the test that contain multiply in name

import mathlib
import pytest
import sys
#dont want to run this test or skip it
# commad to see the skip reason
# pytest -v -rxs
@pytest.mark.skip(reason="I dont want to run this test at the moment")
def test_cal_total():
    total = mathlib.cal_total(4,5)
    assert total == 9

# skip if test meet certain condition
@pytest.mark.skipif(sys.version_info > (3,5), reason="I dont want to run this test if python version is > 3.5")
def test_cal_totalval():
    total = mathlib.cal_total(4,5)
    assert total == 9

def test_cal_multiply():
    result = mathlib.calc_multiply(10,3)
    assert result == 30

# use custom markers to run test on relative os
# dont want to use k command with name of function then use custom markers
# pytest -m mac -v
# pytest -m "not windows" -v --> if you run all test except windows
@pytest.mark.windows
def test_window_1():
    assert True

@pytest.mark.windows
def test_window_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True