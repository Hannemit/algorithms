from typing import Union
import numpy as np


def find_max(input_list: list) -> Union[float, int]:
    """
    Find max of a list (if multiple max values, still just return that value). If list is empty, return nan
    :param input_list: list, our input list
    :return: scalar, the max value in the list.
    """
    if not input_list:
        return np.nan

    max_val = input_list[0]
    for ii, value in enumerate(input_list[1:]):
        if value > max_val:
            max_val = value
    return max_val


def find_min(input_list: list) -> Union[float, int]:
    """
    Find min of a list. If list is empty, return nan
    :param input_list: list, input
    :return: scalar, min value of list
    """
    if not input_list:
        return np.nan

    min_val = input_list[0]
    for ii, value in enumerate(input_list[1:]):
        if value < min_val:
            min_val = value
    return min_val


def selection_sort(input_list: list, ascending: bool = True) -> list:
    """
    Use selection sort to sort a list. Default is ascending.
    :param input_list: list, our input list
    :param ascending: boolean, whether to sort ascending or descending
    :return: list, sorted.
    """
    sorted_list = [0]*len(input_list)

    for ii, value in enumerate(input_list.copy()):
        if ascending:
            val = find_min(input_list)
        else:
            val = find_max(input_list)
        sorted_list[ii] = val
        input_list.remove(val)
    return sorted_list


def quick_sort():
    pass


def bubble_sort():
    pass


def insertion_sort():
    pass


def merge_sort():
    pass


if __name__ == "__main__":
    inputs = [-4.1456, -39, -4.1454, 9.76, 3.2, 0, -1, 0, -2.0]
    inputs2 = [3, 6, 8, 6, 4, 5, 6, 8, 5, 2, 1]

    out = selection_sort(inputs, ascending=False)
    out2 = selection_sort(inputs2, ascending=False)
    print(selection_sort([], ascending=False))
    print(out)
    print(out2)