import pytest
from algorithms import binary_search
test_data = [
    ([1, 2, 4, 6, 12, 32, 42, 52, 64, 72, 90, 123, 245], 32, 5),
    ([2, 3, 4, 5, 6], 2, 0),
    ([2, 3, 4, 5, 6, 7], 9, -1),
    ([2, 3, 4, 5, 6, 7], 7, 5),
    ([1, 2, 3, 4], 7, -1),
]


@pytest.mark.parametrize("test_input, value, expected", test_data)
def test_binary_search(test_input, value, expected):
    out = binary_search.binary_search(test_input, value)
    assert out == expected


