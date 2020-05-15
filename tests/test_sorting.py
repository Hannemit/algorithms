import pytest
from algorithms import sorting
import numpy as np

test_data = [
    ([3, 6, 8, 6, 4, 5, 6, 8, 5, 2, 1], [1, 2, 3, 4, 5, 5, 6, 6, 6, 8, 8]),
    ([], []),
    ([3], [3]),
    (
        [-4.1456, -39, -4.1454, 9.76, 3.2, 0, -1, 0, -2.0],
        [-39, -4.1456, -4.1454, -2, -1, 0, 0, 3.2, 9.76],
    ),
    ([1, 1, 1, 2, 2, 2, 3, 3, 4, 5], [1, 1, 1, 2, 2, 2, 3, 3, 4, 5]),
    ([-1, -2, -1, -2, -4, 5, 3, 9, -4, 2], [-4, -4, -2, -2, -1, -1, 2, 3, 5, 9]),
]

test_data_2 = [
    ([1, 5, 3, 7, 5, 6, 3, 8, 9], 3, [3, 5, 3, 1, 5, 6, 7, 8, 9]),
    ([], 0, []),
    ([8, 9], 1, [8, 9]),
    ([8, 9], 0, [8, 9]),
    ([8, 9, 1, 3], 0, [3, 1, 8, 9]),
    ([8, 9, 1, 3], 2, [1, 9, 8, 3]),
]


@pytest.mark.parametrize("test_input,expected", test_data)
def test_selection_sort(test_input, expected):
    out = sorting.selection_sort(test_input.copy())
    np.testing.assert_allclose(expected, out, atol=1e-5)

    out_descending = sorting.selection_sort(test_input.copy(), ascending=False)
    np.testing.assert_allclose(expected[::-1], out_descending)


@pytest.mark.parametrize("test_input, expected", test_data)
def test_quicksort(test_input, expected):
    out = sorting.quick_sort(test_input.copy())
    out2 = sorting.quick_sort(test_input.copy(), method="med3")
    out3 = sorting.quick_sort(test_input.copy(), method="random")

    np.testing.assert_allclose(expected, out)
    np.testing.assert_allclose(expected, out2)
    np.testing.assert_allclose(expected, out3)


@pytest.mark.parametrize("test_input, expected", test_data)
def test_bubblesort(test_input, expected):
    out = sorting.bubble_sort(test_input.copy())
    np.testing.assert_allclose(expected, out)


@pytest.mark.parametrize("test_input, expected", test_data)
def test_insertionsort(test_input, expected):
    out = sorting.insertion_sort(test_input.copy())
    np.testing.assert_allclose(expected, out)


@pytest.mark.parametrize("test_input, expected", test_data)
def test_mergesort(test_input, expected):
    copy_in = test_input.copy()
    sorting.merge_sort(copy_in, 0, len(copy_in) - 1)
    np.testing.assert_allclose(expected, copy_in)


@pytest.mark.parametrize("test_input, expected", test_data)
def test_heapsort(test_input, expected):
    copy_in = test_input.copy()
    out = sorting.Heap().heap_sort(copy_in)
    np.testing.assert_allclose(expected, out)


@pytest.mark.parametrize("input_list, pivot_idx, expected", test_data_2)
def test_partition_inplace(input_list, pivot_idx, expected):
    copy_in = input_list.copy()
    sorting.partition_inplace(copy_in, pivot_idx)
    assert copy_in == expected
