import pytest
from algorithms import multiplication

test_data = [
    (3, 5, 15),
    (20, 3, 60),
    (1, 23, 23),
    (1, 1, 1),
    (0, 239, 0),
    (12345, 23456, 289564320),
    (123423255, 232346456, 28676955887234280),
    (12, 13, 156),
    (1239673, 12, 14876076),
    (5638, 46529, 262330502),
]


@pytest.mark.parametrize("n1, n2, expected", test_data)
def test_karatsuba(n1, n2, expected):
    out = multiplication.karatsuba(n1, n2)
    assert out == expected
