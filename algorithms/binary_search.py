def binary_search(array, value) -> int:
    """
    Perform binary search to find the index of 'value' in our array. If the value is is not the array, return -1
    :param array: input array
    :param value: value we want index of
    :return: int, index of value in array, or -1 if value not in array
    """
    mid = len(array) // 2
    left = 0
    right = len(array) - 1

    if value > array[right] or value < array[left]:
        return -1

    while True:
        if value < array[mid]:
            right = mid
        else:
            left = mid
        mid = (right + left) // 2

        if array[mid] == value:
            return mid

        if mid == left:
            if value == array[right]:
                return right


def recursive_binary_search(array, value) -> int:
    """
    Perform binary search recursively
    :param array:
    :param value:
    :return:
    """
