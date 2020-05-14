import pytest
from algorithms import closest_points

test_data = [
    ([1, 2, 5, 8, 12], (1, 2)),
    ([1, 1, 1], (1, 1)),
    ([], ()),
    ([3], ()),
    ([6, 32, -3.7, 45, 13, -5, 374, 13], (13, 13)),
    ([6, 32, 87, 45, 13, 75, 374, 51], (45, 51)),
    ([6, 32, 87, 45, 13, 75, 374, 52], (6, 13)),
    ([374, 32, 87, 45, -24, 75, 6, 52, 13], (6, 13)),
    ([23, 4, 9, 16, 22, 1, 10], (9, 10)),
]


@pytest.mark.parametrize("input_list, expected", test_data)
def test_find_closest_1d(input_list, expected):
    out = closest_points.find_closest_1d(input_list)
    assert out == expected
