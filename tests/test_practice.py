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

test_data_2 = [
    ([1, 1, 2, 8, 1, 2, 5], 9),
    ([1, 2], 2),
    ([5, 4], 1),
    ([1, 2, 3, 4, 5, 4, 3], 3),
    ([3], 1),
    ([1], 1),
    ([1, 6, 1, 6, 1], 4),
    ([1, 2, 1, 2, 1, 2], 13),
    ([1, 2, 1, 2, 1, 2, 1, 1], 34),
    ([1, 2, 1, 2, 1, 2, 7, 1, 2, 1], 13 * 3),
]


test_data_3 = [
    ([0, 2, 1], 3),
    ([3, 4, -1, 1], 2),
    ([1, 7, 5, 8, 12, 3, 5, 4, 9, 1, 6, 7, 3], 2),
    ([1, 7, 5, 8, -3, 12, 3, 5, 4, 9, 1, 6, 7, 3, 2], 10),
    ([5, 6, 7], 1),
    ([9, 2], 1),
    ([-3, -1], 1),
    ([2], 1),
    ([-2], 1),
    ([1], 2),
    ([], 1),
]


test_data_4 = [(4, 5), (3, 3), (1, 1), (0, 1), (5, 8)]


@pytest.mark.parametrize("input_arr, k, expected", test_data)
def test_get_kth_from_end(input_arr, k, expected):
    llist = practice.List()
    llist.create_list(input_arr)

    out = practice.get_kth_from_end(llist.head, k)

    if expected is None:
        assert out is None
    else:
        assert out == expected


@pytest.mark.parametrize("input_list, expected", test_data_2)
def test_find_all_combs(input_list, expected):
    out = practice.find_all_combs(input_list)
    assert out == expected


@pytest.mark.parametrize("input_list, expected", test_data_3)
def test_find_first_missing_pos_int(input_list, expected):
    out = practice.find_first_missing_pos_int(input_list.copy())
    assert out == expected


@pytest.mark.parametrize("input_steps, expected", test_data_4)
def test_get_unique_steps(input_steps, expected):
    out = practice.get_unique_steps(input_steps)
    assert out == expected


def test_fib():
    outputs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for ii in range(11):
        assert practice.fibonacci_iter(ii) == outputs[ii]
        assert practice.fibonacci_recursive(ii) == outputs[ii]
