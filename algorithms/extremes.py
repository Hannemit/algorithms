from collections import deque


def find_max_rec(input_list: list):
    # find the highest number in an input list with all distinct numbers
    # assume length of input_list is a power of 2
    if len(input_list) == 2:
        if input_list[0] > input_list[1]:
            return input_list[0]
        else:
            return input_list[1]

    mid = len(input_list) // 2
    max1 = find_max_rec(input_list[:mid])
    max2 = find_max_rec(input_list[mid:])

    if max1 < max2:
        return max2
    else:
        return max1


def find_second_highest(input_list: list):
    # TODO: this function wrong at moment, the max and second max can be in same partition.
    mid = len(input_list) // 2

    max1 = find_max_rec(input_list[:mid])
    max2 = find_max_rec(input_list[mid:])

    if max1 > max2:
        return max2
    else:
        return max1


def find_max_subarrays(input_list: list, len_subarr: int):
    if len(input_list) == 0:
        return []

    store_answers = []
    double_ended = deque([0])

    for i in range(1, len_subarr):

        while double_ended and input_list[i] >= double_ended[-1]:
            double_ended.pop()
        double_ended.append(i)

    for i in range(len_subarr, len(input_list)):
        # print max of subarray
        print(input_list[double_ended[0]])
        store_answers.append(input_list[double_ended[0]])

        while input_list[i] >= input_list[double_ended[-1]]:
            double_ended.pop()

        if input_list[i] > input_list[double_ended[0]]:
            double_ended.clear()
            double_ended.append(i)
        else:
            # clear any indices not in current window ([i - k + 1, i])
            try:
                double_ended.remove(i - len_subarr)
            except ValueError:
                pass

            # insert new element in correct position
            for j in range(len(double_ended) - 1, -1, -1):
                if input_list[i] > input_list[double_ended[j]]:
                    double_ended.pop()
            double_ended.append(i)
    # print last time
    print(input_list[double_ended[0]])
    store_answers.append(input_list[double_ended[0]])
    return store_answers


if __name__ == "__main__":

    # inputs = [6, 9, 1, 5, 3, 13, 15, 4, 12, 2, 7, 10, 11, 8, 16, 14]
    # print(find_second_highest(inputs))

    inputs = [10, 5, 2, 7, 8, 7]
    find_max_subarrays(inputs, 3)
