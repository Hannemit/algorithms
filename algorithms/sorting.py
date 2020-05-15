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
    sorted_list = [0] * len(input_list)

    for ii, value in enumerate(input_list.copy()):
        if ascending:
            val = find_min(input_list)
        else:
            val = find_max(input_list)
        sorted_list[ii] = val
        input_list.remove(val)
    return sorted_list


def pick_pivot(in_list: list, method: str):
    if method == "random":
        return np.random.choice(in_list)
    elif method == "med3":
        vals = np.random.choice(in_list, size=3, replace=False)
        return np.median(vals)
    elif method == "med5":
        vals = np.random.choice(in_list, size=5, replace=False)
        return np.median(vals)
    else:
        return in_list[0]


def partition_using_pivot(input_list: list, pivot: Union[float, int]):
    less_than = []
    greater_than = []
    for value in input_list:
        if value <= pivot:
            less_than.append(value)
        else:
            greater_than.append(value)
    return less_than, greater_than


def partition_inplace(input_list: list, pivot_idx: int):
    # partition in place, using constant space.
    if len(input_list) < 2:
        return input_list

    if pivot_idx != 0:
        swap_values(input_list, pivot_idx, 0)

    pivot = input_list[0]
    ii = 1
    for k in range(1, len(input_list)):
        if input_list[k] < pivot:
            swap_values(input_list, k, ii)
            ii += 1
    swap_values(input_list, 0, ii - 1)


def quick_sort(in_list: list, method: str = "random"):

    if len(in_list) < 2:
        return in_list

    # pick pivot
    pivot = pick_pivot(in_list, method=method)

    in_list.remove(pivot)
    less_than_piv, greater_than_piv = partition_using_pivot(in_list, pivot)

    return quick_sort(less_than_piv) + [pivot] + quick_sort(greater_than_piv)


def bubble_sort(input_list: list) -> list:
    """
    TODO: make inplace
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


def insertion_sort(input_list: list) -> list:
    """
    TODO: make in-place, no need to return list.
    Insertion sort is also O(n^2) but it is still more efficient than bubble sort or selection sort. It is not bad for
    arrays that are already close to being sorted. The running order is O(kn) if each element is no more than k places
    away from its sorted position (so if completely unsorted, then get O(n*n))
    It is stable, meaning it does not change the relative order of elements with the same value.
    It's in-place, so space complexity is O(1)
    It's also online, so it can create the sorted list as it gets new elements.
    :param input_list: list, the list we want to sort
    :return: list, the sorted input list
    """
    length = len(input_list)

    for ii in range(1, length):

        value = input_list[ii]
        j = ii - 1
        while value < input_list[j] and j >= 0:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = value
    return input_list


def merge(list_: list, start: int, mid: int, end: int):
    """
    Merge two lists so that they are sorted afterwards. Example:
    list_ = [3, 5, 2, 4, 1, 6]
    start = 0
    mid = 1
    end = 2
    We merge the arrays [3, 5] and [2], and return [2, 3, 5]
    :param list_: list, the input list
    :param start: int, index of the start of the first sublist
    :param mid: int, index of the end (inclusive) of the first sublist. Second sublist starts at mid + 1
    :param end: int, index of end (inclusive) of the second sublist
    :return: list, a sorted part of the input list_ in interval [start, end]
    """
    i, j, k = start, mid + 1, 0
    new_list = [0] * (end - start + 1)

    # continue until one of the lists completely done
    while i <= mid and j <= end:
        if list_[i] <= list_[j]:
            new_list[k] = list_[i]
            i += 1
        else:
            new_list[k] = list_[j]
            j += 1
        k += 1

    # continue with other list (if not done yet)
    while i <= mid:
        new_list[k] = list_[i]
        i += 1
        k += 1

    # continue with other list (if not done yet)
    while j <= end:
        new_list[k] = list_[j]
        j += 1
        k += 1

    # change original list
    for i in range(start, end + 1):
        try:
            list_[i] = new_list[i - start]
        except IndexError:
            raise IndexError


def merge_sort(input_list: list, left: int, right: int) -> None:
    """
    Perform merge-sort algorithm to sort a list in-place. Merge sort has time complexity O(n log n), and space
    complexity O(n) as we create new lists in merge(). This new list is usually quite short, we'll have all elements
    in there at some point, so O(n) in total (e.g. first it might be [1, 2, 3] and then [4, 5, 6], etc..
    :param input_list: list, input that we want to sort
    :param left: int, left index from where we start sorting
    :param right: int, right index from where we start sorting
    :return: None, sorts in-place
    """
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(input_list, left, mid)
    merge_sort(input_list, mid + 1, right)
    merge(input_list, left, mid, right)


def swap_values(input_list, idx1, idx2):
    temp = input_list[idx1]
    input_list[idx1] = input_list[idx2]
    input_list[idx2] = temp
    return input_list


class Heap:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def _heapify(self, root_idx: int) -> None:
        """
        Make sure the subtree from root_idx down is a heap. We push root_idx down until it reached the correct
        location
        :param root_idx: int, index of root of the current subtree
        :return: None, updates self.heap
        """
        max_iter = self.heap_size // 2
        node_idx = root_idx
        while node_idx < max_iter:
            idx_child_1 = 2 * node_idx + 1
            idx_child_2 = idx_child_1 + 1
            if idx_child_2 > self.heap_size - 1:
                idx_swap = idx_child_1
            else:
                if self.heap[idx_child_1] > self.heap[idx_child_2]:
                    idx_swap = idx_child_1
                else:
                    idx_swap = idx_child_2
            if self.heap[node_idx] < self.heap[idx_swap]:
                self.heap = swap_values(self.heap, node_idx, idx_swap)
                node_idx = idx_swap
            else:
                break

    def _pop(self):
        """
        Pop off the top value
        :return: the top value of the heap
        """
        if self.heap_size == 0:
            raise RuntimeError("Cannot pop from empty heap")

        top_value = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self._heapify(0)
        return top_value

    def _create_heap(self, input_list: list) -> None:
        """
        Given some input list (or array), make a max heap out of it
        :param input_list: inputs we want to create a max heap for
        :return: None, updates self.heap and self.heap_size
        """
        mid_idx = (
            len(input_list) // 2
        )  # every node to the right of this (and itself) is a leaf
        self.heap = input_list
        self.heap_size = len(input_list)
        for ii in range(1, mid_idx + 1):
            self._heapify(mid_idx - ii)

    def heap_sort(self, input_list: list, ascending: bool = True) -> list:
        """
        Sort a given input list using heap sort
        :param input_list: list, our input list
        :param ascending: boolean, if True sort in ascending order, otherwise descending
        :return: list, the sorted list
        """
        self._create_heap(input_list)
        descending_list = [self._pop() for _ in range(self.heap_size)]
        if ascending:
            return descending_list[::-1]
        else:
            return descending_list


###################################


def insertion_sort_recursive():
    pass


def cocktail_sort():
    pass


def comb_sort():
    pass


def radix_sort():
    pass


if __name__ == "__main__":
    inputs = [-4.1456, -39, -4.1454, 9.76, 3.2, 0, -1, 0, -2.0]
    inputs2 = [3, 6, 8, 6, 4, 5, 6, 8, 5, 2, 1]
    inputs2 = [-1, -2, -1, -2, -4, 5, 3, 9, -4, 2]

    print(Heap().heap_sort(inputs2, ascending=False))
