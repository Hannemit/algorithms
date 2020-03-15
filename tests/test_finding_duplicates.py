import pytest
from algorithms import finding_duplicates
import numpy as np

test_data = [
    ([1, 2, 2, 3], 2),
    ([1, 3, 4, 2, 3, 5, 2], 3),
    ([1, 2, 3, 4, 5, 6, 7], -1),
    ([-2, 2, -3, 0, 9, 4, 0, -5], 0)
]


@pytest.mark.parametrize("inputs, expected", test_data)
def test_finding_duplicates(inputs, expected):
    out = finding_duplicates.find_duplicates(inputs)
    np.testing.assert_allclose(out, expected)
