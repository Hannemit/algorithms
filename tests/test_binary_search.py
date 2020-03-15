import pytest
from algorithms import binary_search
test_data = [
    ([1, 2, 4, 6, 12, 32, 42, 52, 64, 72, 90, 123, 245], 32, 5),
    ([2, 3, 4.4, 5, 6.8], 2, 0),
    ([2, 3, 4, 5, 6, 7], 7, 5),
    ([2, 3, 4, 5, 6, 7.2], 9, -1),
    ([1, 2, 3.3, 4], 0, -1),
    ([], 3, -1),
    ([-10.2, -5, -3, 0, 3, 5, 8], -5, 1),
    ([-10, -5, -3, 0, 3, 5, 8], -10, 0),
    ([-10, -5, -3, 0, 3, 5, 8], 3, 4),
    ([-20, -15, -10, -5, -3, -2, -1], -5, 3),
    ([-20.643, -10.0, 6.4, 7.6, 8.12], 7.5, -1),
    ([-20.643, -10.0, 6.4, 7.6, 8.12], 7.6, 3),
]


@pytest.mark.parametrize("test_input, value, expected", test_data)
def test_binary_search(test_input, value, expected):
    out = binary_search.binary_search(test_input, value)
    assert out == expected


@pytest.mark.parametrize("test_input, value, expected", test_data)
def test_recursive_binary_search(test_input, value, expected):
    out = binary_search.recursive_binary_search(test_input, 0, len(test_input) - 1, value)
    assert out == expected
