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


def pick_pivot(arr, method: str):
    if method == "first":
        return arr[0]
    elif method == "random":
        return np.random.choice(arr)
    elif method == "med3":
        vals = np.random.choice(arr, size=3, replace=False)
        return np.median(vals)
    elif method == "med5":
        vals = np.random.choice(arr, size=5, replace=False)
        return np.median(vals)


def partition_using_pivot(input_list, pivot):
    less_than = []
    greater_than = []
    for value in input_list:
        if value <= pivot:
            less_than.append(value)
        else:
            greater_than.append(value)
    return less_than, greater_than


def quick_sort(in_list, method="first"):

    if len(in_list) < 2:
        return in_list

    # pick pivot
    pivot = pick_pivot(in_list, method=method)

    in_list.remove(pivot)
    less_than_piv, greater_than_piv = partition_using_pivot(in_list, pivot)

    return quick_sort(less_than_piv) + [pivot] + quick_sort(greater_than_piv)


def bubble_sort(input_list: list) -> list:
    """
    In practice, very slow algorithm. Both average and worst-case are O(n^2). The only good thing about it is that if
    the input list was already sorted, it runs in O(n), as opposed to many other sorting algorithms which still take
    O(n log n) even if the array was already sorted (as they don't check for that). However, insertion sort has the
    same advantage and performs better than bubble sort. So in practice, never use bubble sort.

    The largest element wins every swap, and therefore moves straight away to the end of the array (assuming we're
    sorting from low to high). It can take place in successive swaps, so it just keeps going. A very small element only
    moves a single step per pass through the array. It just goes down, as a larger element is moved up past it. If the
    smallest element is at the end of the list, it takes n - 1 steps to get to the start. Whereas the largest element
    only takes 1 step to get to the end. This is why small elements are called turtles, and large elements rabbits.

    There are variations of bubble sort that try to improve the speed of the turtles, e.g. cocktail sort and comb sort.
    Bubble sort is stable, i.e. it does not change the relative order of elements with the same value

    :param input_list: input list
    :return: list, sorted version of input_list. Default is sort from low to high
    """
    have_switched = True
    length = len(input_list)

    while have_switched:
        have_switched = False
        for ii in range(1, length):
            value = input_list[ii - 1]
            value_next = input_list[ii]

            if value > value_next:
                input_list[ii - 1] = value_next
                input_list[ii] = value
                have_switched = True
        length -= 1

    return input_list


def insertion_sort(input_list):
    """
    Insertion sort is also O(n^2) but it is still more efficient than bubble sort or selection sort. It is not bad for
    arrays that are already close to being sorted. The running order is O(kn) if each element is no more than k places
    away from its sorted position (so if completely unsorted, then get O(n*n))
    It is stable, meaning it does not change the relative order of elements with the same value.
    It's in-place, so space complexity is O(1)
    It's also online, so it can create the sorted list as it gets new elements.
    :return:
    """
    length = len(input_list)

    for ii in range(1, length):

        value = input_list[ii]
        j = ii - 1
        while value < input_list[j] and j >= 0:
            input_list[j+1] = input_list[j]
            j -= 1
        input_list[j + 1] = value
    return input_list


def merge_sort(input_list):
    """
    Perform merge sort
    :param input_list:
    :return:
    """
    pass


###################################


def insertion_sort_recursive():
    pass


def cocktail_sort():
    pass


def comb_sort():
    pass


def heap_sort():
    pass


if __name__ == "__main__":
    inputs = [-4.1456, -39, -4.1454, 9.76, 3.2, 0, -1, 0, -2.0]
    inputs2 = [3, 6, 8, 6, 4, 5, 6, 8, 5, 2, 1]

    out = insertion_sort(inputs2)
