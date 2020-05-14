import pytest
from algorithms import inversions

test_data = [
    ([[1, 3, 5], [2, 4, 6]], [1, 2, 3, 4, 5, 6], 3),
    ([[], [2, 3, 7, 12, 34]], [2, 3, 7, 12, 34], 0),
    ([[], []], [], 0),
    ([[1, 3, 4], [2, 4, 6]], [1, 2, 3, 4, 4, 6], 2),
    ([[1, 2, 3], [4, 5, 6, 7]], [1, 2, 3, 4, 5, 6, 7], 0),
    (
        [[1, 2, 4, 6, 8], [-4, -1, 0, 3, 5, 7, 9]],
        [-4, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        21,
    ),
]

test_data_2 = [
    ([1, 3, 5, 2, 4, 6], [1, 2, 3, 4, 5, 6], 3),
    ([6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], 15),
    ([], [], 0),
    ([1], [1], 0),
    ([1, 2, 3], [1, 2, 3], 0),
    ([3, 1], [1, 3], 1),
]


@pytest.mark.parametrize("input_lists, output_list, exp_num_inversions", test_data)
def test_count_split_inversions(input_lists, output_list, exp_num_inversions):

    out, num_inversions = inversions.count_split_inversions(
        input_lists[0], input_lists[1]
    )
    assert out == output_list
    assert num_inversions == exp_num_inversions


@pytest.mark.parametrize("input_list, output_list, exp_num_inversions", test_data_2)
def test_sort_and_count_inversions(input_list, output_list, exp_num_inversions):

    out, num_inversions = inversions.sort_and_count_inversions(input_list)
    assert out == output_list
    assert num_inversions == exp_num_inversions
