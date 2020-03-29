import numpy as np


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
