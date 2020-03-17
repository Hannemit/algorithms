"""
https://medium.com/solvingalgo/solving-algorithmic-problems-find-a-duplicate-in-an-array-3d9edad5ad41
Site has some good examples of different ways of solving it.
"""

"""
These functions all solve the problems of:
Given an array of n + 1 integers between 1 and n, find one of the duplicates.
If there are multiple possible answers, return one of the duplicates.
If there is no duplicate, return -1.
"""


def find_duplicates_storing(input_list: list):
    """
    Given an input list, return the first duplicate we see. If there are multiple duplicates, we just return one of
    them. E.g. input list is [1, 2, 2, 3, 3] --> return 2. IF no duplicate found, return -1. Example: [1, 2, 3] --> -1
    This has O(n) time complexity but also O(n) space complexity as we need a second structure to keep track of which
    numbers we've already seen.
    :param input_list:
    :return:
    """
    items_seen = set()

    for value in input_list:
        if value in items_seen:
            return value
        else:
            items_seen.add(value)
    return -1


def find_duplicates_sorting(input_list: list):
    """
    First sort the array, then only check the neighbours. This is O(1) in space complexity since we don't create any
    extra array to store stuff in, but O(n log n) in time complexity because we have to sort the list up front.
    :param input_list:
    :return:
    """
    # first sort the input list
    input_list.sort()

    # then only need to check the element next to the current element
    for i in range(len(input_list) - 1):
        if input_list[i] == input_list[i + 1]:
            return input_list[i]
    return -1


def find_duplicates_third_method():
    pass
