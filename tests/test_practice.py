import pytest
from algorithms import practice

test_data = [
    ([1, 2, 3, 4, 5, 6, 7], 2, 6),
    ([1], 2, None),
    ([], 2, None),
    ([1, 4], 1, 4),
    ([1, 2, 3, 4, 5, 6, 7, 3, 2, 1], 5, 6),
    ([1, 2, 3, 4, 5, 6, 7, 3, 2, 1], 9, 2),
    ([1, 2, 3, 4, 5, 6, 7, 3, 2, 1], 10, 1),
    ([1, 2, 3, 4, 5, 6, 7, 3, 2, 1], 11, None),
]


@pytest.mark.parametrize("input_arr, k, expected", test_data)
def test_get_kth_from_end(input_arr, k, expected):
    llist = practice.List()
    llist.create_list(input_arr)

    out = practice.get_kth_from_end(llist.head, k)

    if expected is None:
        assert out is None
    else:
        assert out == expected
