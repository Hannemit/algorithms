def zero_pad(in_string: str, num_zeros: int, left=True) -> str:
    """
    Pad any number of zeros to an input string, at the end or at the start
    :param in_string: string, input
    :param num_zeros: int, number of zeros to add
    :param left: boolean, if True add the zeros on the left side, if False add on the right side
    :return: string, with zeros padded
    """
    zeros = "0" * num_zeros

    if left:
        return zeros + in_string
    else:
        return in_string + zeros


def karatsuba(num_1: int, num_2: int) -> int:
    """
    Use the karatsuba algorithm to compute the product of two integers.
    :param num_1: int
    :param num_2: int
    :return: int, result of num_1 * num_2
    """
    if num_1 < 10 and num_2 < 10:
        return num_1 * num_2

    str1 = str(num_1)
    str2 = str(num_2)

    # make sure both have same length -- to do correct split and zero padding at end
    if len(str1) < len(str2):
        str1 = zero_pad(str1, len(str2) - len(str1), left=True)
    else:
        str2 = zero_pad(str2, len(str1) - len(str2), left=True)

    length = len(str1)
    midpoint = length // 2

    # take care of numbers with odd number of digits
    if length % 2 == 1:
        midpoint += 1

    one = int(str1[:midpoint])
    two = int(str1[midpoint:])
    three = int(str2[:midpoint])
    four = int(str2[midpoint:])

    res1 = karatsuba(one, three)
    res2 = karatsuba(two, four)
    res3 = karatsuba(one + two, three + four)
    res4 = res3 - res1 - res2

    res1 = zero_pad(str(res1), 2 * (length - midpoint), left=False)
    res4 = zero_pad(str(res4), length - midpoint, left=False)

    return int(res1) + res2 + int(res4)
