"""
https://medium.com/solvingalgo/solving-algorithmic-problems-find-a-duplicate-in-an-array-3d9edad5ad41
Site has some good examples of different ways of solving it.
"""
import numpy as np


def find_duplicates_storing(input_list):
    """
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


def find_duplicates_second_method():
    pass


def find_duplicates_third_method():
    pass
