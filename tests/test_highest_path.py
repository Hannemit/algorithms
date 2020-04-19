import pytest
from algorithms import highest_path

test_input = [
    ([[1, 2, 2], [1, 5, 2], [4, 2, 1]], 11),
    ([[0, 20, 50], [0, 1, 10], [100, 0, 0]], 100),
    ([[3]], 3),
]


@pytest.mark.parametrize("input_matrix, expected", test_input)
def test_highest_path(input_matrix, expected):
    out = highest_path.find_best_path(input_matrix)
    assert out == expected
