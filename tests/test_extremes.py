import pytest
from algorithms import extremes

test_data = [
    ([10, 5, 2, 7, 8, 7], 3, [10, 7, 8, 8]),
    ([10, 9, 8, 7, 6, 5, 4], 3, [10, 9, 8, 7, 6]),
    ([], 2, []),
    ([4, 2, 4], 3, [4]),
    ([1, 2, 3, 4, 5, 6, 7, 8], 3, [3, 4, 5, 6, 7, 8]),
    (
        [7, 2, 7, 2, 2, 1, -3, -4, 4, 9, 7, 1, 1, 4],
        3,
        [7, 7, 7, 2, 2, 1, 4, 9, 9, 9, 7, 4],
    ),
]


@pytest.mark.parametrize("input_list, k, expected", test_data)
def test_find_max_subarrays(input_list, k, expected):
    out = extremes.find_max_subarrays(input_list, k)
    assert out == expected
