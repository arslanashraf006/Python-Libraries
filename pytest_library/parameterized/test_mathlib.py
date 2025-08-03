import mathlib
import pytest

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (10,100)
                         ])
def test_cal_square_1(test_input, expected_output):
    result = mathlib.calc_square(test_input)
    assert result == expected_output