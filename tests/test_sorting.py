import pytest
from algorithms import sorting
import numpy as np

test_data = [
    ([3, 6, 8, 6, 4, 5, 6, 8, 5, 2, 1], [1, 2, 3, 4, 5, 5, 6, 6, 6, 8, 8]),
    ([], []),
    ([-4.1456, -39, -4.1454, 9.76, 3.2, 0, -1, 0, -2.0], [-39, -4.1456, -4.1454, -2, -1, 0, 0, 3.2, 9.76]),
]


@pytest.mark.parametrize("test_input,expected", test_data)
def test_selection_sort(test_input, expected):
    out = sorting.selection_sort(test_input.copy())
    np.testing.assert_allclose(expected, out, atol=1e-5)

    out_descending = sorting.selection_sort(test_input.copy(), ascending=False)
    np.testing.assert_allclose(expected[::-1], out_descending)

