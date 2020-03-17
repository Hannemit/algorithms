import pytest
from algorithms import finding_duplicates

test_data = [
    ([1, 2, 2, 3], [2]),
    ([1, 3, 4, 2, 3, 5, 2], [3, 2]),
    ([1, 2, 3, 4, 5, 6, 7], [-1]),
    ([-2, 2, -3, 0, 9, 4, 0, -5], [0]),
    ([], [-1]),
    ([3], [-1]),
    ([-2, 2, -3, 4, 4.01, 2, 3, 4, 4], [2, 4]),
]


@pytest.mark.parametrize("inputs, expected", test_data)
def test_finding_duplicates_storing(inputs, expected):
    out = finding_duplicates.find_duplicates_storing(inputs)
    assert out in expected


@pytest.mark.parametrize("inputs, expected", test_data)
def test_finding_duplicates_sorting(inputs, expected):
    out = finding_duplicates.find_duplicates_sorting(inputs)
    assert out in expected
