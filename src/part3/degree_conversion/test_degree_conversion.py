import pytest
from .main import fahrenheit_to_celsius


class TestDegreeConversions:

    @pytest.mark.parametrize(
        "fahrenheit, expected",
        [
            (212, 100),
            (98.6, 37),
            (70, 21.11111),
            (32, 0),
            (0, -17.77778),
            (-40, -40),
        ],
    )
    def test_fahrenheit_to_celsius(self, fahrenheit, expected):
        result = fahrenheit_to_celsius(fahrenheit=fahrenheit)

        assert result == pytest.approx(expected=expected)
