from typing import Union
import numpy as np


def binary_search(array: Union[list, np.ndarray], value: Union[int, float]) -> int:
    """
    Perform binary search to find the index of 'value' in our array. If the value is is not the array, return -1
    :param array: array-like, input array
    :param value: scalar, value we want index of
    :return: int, index of value in array, or -1 if value not in array
    """
    if len(array) == 0:
        return -1

    left = 0
    right = len(array) - 1
    mid = (left + right) // 2

    if value > array[right] or value < array[left]:
        return -1

    while left <= right:
        if array[mid] == value:
            return mid
        elif value < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

        mid = (right + left) // 2
    return -1


def recursive_binary_search(arr: Union[list, np.ndarray], left: int, right: int, value: Union[float, int]) -> int:
    """
    Perform binary search recursively. Returns -1 if value not in array
    :param arr: array or list, the array we want to search in
    :param left: int, defines the left boundary of the array we search in. Should be initially set to 0
    :param right: int, defines the right boundary of the array we search in. Should be initially set to len(arr) - 1
    :param value: scalar, the value we're looking for
    :return: int, index of value in array. Return -1 if value not in array
    """

    # this is not necessarily required but saves time if value outside and array very long
    if len(arr) > 0 and (value < arr[left] or value > arr[right]):
        return -1

    # do the binary search
    if right >= left:
        mid = (left + right) // 2

        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return recursive_binary_search(arr, left, mid - 1, value)
        else:
            return recursive_binary_search(arr, mid + 1, right, value)
    else:
        return -1  # element not present
