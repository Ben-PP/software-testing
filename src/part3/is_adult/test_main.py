import pytest
from .main import is_adult


class TestIsAdult:

    @pytest.mark.parametrize(
        "age, expected",
        [
            (0, False),
            (1, False),
            (16, False),
            (17, False),
            (18, True),
            (19, True),
            (100, True),
            (150, True),
        ],
    )
    def test_is_adult(self, age: int, expected: bool):
        assert is_adult(age) == expected

    @pytest.mark.parametrize(
        "age",
        [-1, -2, -100],
    )
    def test_is_adult_exceptions(self, age: int):
        with pytest.raises(
            ValueError, match=r"Age must be a positive integer, but got -\d+"
        ):
            is_adult(age)
