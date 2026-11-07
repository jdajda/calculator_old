import pytest
from calculator import Calculator



class TestCalculator:
    def test_sum(self):
        calc = Calculator(1, 2)
        assert calc.sum() == 3


    @pytest.mark.parametrize("a, b, expected", [
            (2, 3, 5),
            (-1, -2, -3),
            (2.5, 3.5, 6.0),
    ])

    def test_add_parametrized(self, a, b, expected):
        calc = Calculator(a, b)
        assert calc.sum() == expected