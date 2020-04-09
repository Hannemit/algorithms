import numpy as np
from typing import List


def swap_min_max(arr: np.ndarray):
    try:
        min_idx = np.argmin(arr)
        max_idx = np.argmax(arr)
    except ValueError:
        return arr

    min_val = arr[min_idx]
    arr[min_idx] = arr[max_idx]
    arr[max_idx] = min_val

    return arr


def factorial(number: int):
    if not isinstance(number, int):
        raise TypeError(f"input must be int, not {type(number)}")

    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


def choose_pivot(input_list):
    return input_list[0]


def get_both_sides(input_list, pivot):
    less_than = []
    greater_than = []

    for value in input_list:
        if value <= pivot:
            less_than.append(value)
        else:
            greater_than.append(value)
    return less_than, greater_than


def quicksort(input_list: list) -> list:

    if len(input_list) <= 1:
        return input_list

    pivot = choose_pivot(input_list)
    input_list.remove(pivot)
    less_than_pivot, more_than_pivot = get_both_sides(input_list, pivot)

    return quicksort(less_than_pivot) + [pivot] + quicksort(more_than_pivot)


def all_chars_unique(string: str):
    chars = set()
    for char in string:
        if char in chars:
            return False
        chars.add(char)
    return True


def find_max(input_list: List[int], high=True) -> (int, int):
    """
    Find max of a list and its index. If multiple maxes, just either the one with lowest or highest index, depending
    on 'high'
    :param input_list: list, our input list
    :param high: boolean, if True then if multiple max values return the highest index one, otherwise return
            the lowest index one
    :return: (max_val, idx_max_val), the max value and its index
    """
    if not input_list:
        raise ValueError("Provide valid list.., not empty one")

    max_val = input_list[0]
    max_idx = 0
    for ii, value in enumerate(input_list[1:]):
        if high:
            if value >= max_val:
                max_val = value
                max_idx = ii + 1
        else:
            if value > max_val:
                max_val = value
                max_idx = ii + 1
    return max_val, max_idx


def calculate_water_volume(heights: List[int]) -> int:
    if not heights:
        return 0

    total_num = len(heights)
    max_val_list = heights.copy()

    # fill in max values from left to right
    for i in range(1, total_num):
        max_val_list[i] = max(heights[i], max_val_list[i - 1])

    # and from right to left, picking min of the maxes
    max_val_list[-1] = heights[-1]
    total_sum = 0
    for i in range(total_num - 2, 0, -1):
        max_val_list[i] = min(max_val_list[i], max(heights[i], max_val_list[i + 1]))
        total_sum += max_val_list[i] - heights[i]
    return total_sum


if __name__ == "__main__":

    input_height = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
    result = calculate_water_volume(input_height)
    print(result)
