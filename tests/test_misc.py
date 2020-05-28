import pytest
from algorithms import misc
import numpy as np


test_data = [(4, 24), (0, 1), (1, 1), (10, 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2), (-3, 1)]

test_data2 = [
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


test_data_3 = [
    ([1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2], 15),
    ([2, 2, 2, 2], 0),
    ([1, 2, 3, 4, 5], 0),
    ([5, 4, 3, 2], 0),
    ([1], 0),
    ([1, 4], 0),
    ([], 0),
    ([5, 4, 3, 2, 3, 4, 7], 9),
    ([2, 3, 4, 5, 4, 3, 2], 0),
    ([5, 1, 1, 1, 5], 12),
    ([5, 0, 0, 4, 3, 5], 13),
    ([2, 3, 4, 3, 3, 2, 4], 4),
]


test_data_4 = [
    ([1, 2, 3], [6, 3, 2]),
    ([0, 1, 5, 3], [15, 0, 0, 0]),
    ([1], []),
    ([], []),
    ([9, 3, 1, 5, 2], [30, 90, 270, 54, 135]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([4, 2], [2, 4]),
]


@pytest.mark.parametrize("input_number, expected", test_data)
def test_factorial(input_number, expected):
    out = misc.factorial(input_number)
    assert out == expected

    with pytest.raises(TypeError):
        misc.factorial(3.5)


@pytest.mark.parametrize("test_input, expected", test_data2)
def test_quicksort(test_input, expected):
    out = misc.quicksort(test_input.copy())
    out2 = misc.quicksort(test_input.copy())
    out3 = misc.quicksort(test_input.copy())

    np.testing.assert_allclose(expected, out)
    np.testing.assert_allclose(expected, out2)
    np.testing.assert_allclose(expected, out3)


@pytest.mark.parametrize("test_input, expected", test_data_3)
def test_calculate_water_volume(test_input, expected):
    out = misc.max_water_constant_space(test_input.copy())
    np.testing.assert_equal(out, expected)

    out = misc.calculate_water_volume(test_input.copy())
    np.testing.assert_equal(out, expected)


@pytest.mark.parametrize("test_input, expected", test_data_4)
def test_production_except_self_2(test_input, expected):
    out = misc.product_except_self(test_input.copy())
    np.testing.assert_equal(out, expected)
