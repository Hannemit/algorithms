def count_split_inversions(left: list, right: list) -> (list, int):
    """
    Merge two sorted input arrays, keep track of number of inversions
    :param left: list, sorted
    :param right: right, sorted
    :return: (list, int), the overall sorted list and the number of inversions in [left, right] flattened list
    """
    merged_arr = [0] * (len(left) + len(right))

    i = j = k = num_inversions = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr[k] = left[i]
            i += 1
        else:
            merged_arr[k] = right[j]
            j += 1
            num_inversions += len(left[i:])
        k += 1

    while i < len(left):
        merged_arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged_arr[k] = right[j]
        j += 1
        k += 1

    return merged_arr, num_inversions


def sort_and_count_inversions(input_list: list) -> (list, int):
    length = len(input_list)

    if length <= 1:
        return input_list, 0

    left = input_list[: length // 2]
    right = input_list[length // 2:]

    left_sorted, left_count = sort_and_count_inversions(left)
    right_sorted, right_count = sort_and_count_inversions(right)
    all_sorted, split_count = count_split_inversions(left_sorted, right_sorted)

    return all_sorted, left_count + right_count + split_count


if __name__ == "__main__":

    inputs = [[1, 2, 3], [4, 5, 6, 7]]

    count_split_inversions(inputs[0], inputs[1])

    # read in lots of numbers
    numbers = []
    with open("../data/numbers_inversion_count.txt") as f:
        for line in f:
            numbers.append(int(line))

    # now calculate the number of inversions
    _, num_inv = sort_and_count_inversions(numbers)
    print(num_inv)
