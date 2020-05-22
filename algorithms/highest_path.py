from typing import List, Union
import queue


def find_best_path(mat: List[List[int]]) -> int:
    """
    Given a 2D matrix of ints with n rows and m cols, find the path from (0, 0) to (n, m) with the highest
    overall score, where the score of each individual element is just the integer stored there.
    You can only take n + m - 2 steps (so no going back and forth).
    :param mat: list of lists, our matrix
    :return: int, the max score you can get by taking the best path.
    """
    num_cols = len(mat[0])
    num_rows = len(mat)

    if num_cols < 1 and num_rows < 1:
        raise ValueError("please input matrix with at least 1 row and 1 column")

    for i in range(num_rows):
        for j in range(num_cols):
            # look at value at index [i][j -1] and [i-1][j], add current value to the max of those.
            if i == 0:
                if j == 0:
                    continue
                mat[i][j] += mat[i][j - 1]
            elif j == 0:
                mat[i][j] += mat[i - 1][j]
            else:
                mat[i][j] += max(mat[i][j - 1], mat[i - 1][j])

    return mat[num_rows - 1][num_cols - 1]


def find_shortest_maze_path(
    mat: List[List[bool]], start: List[int], end: List[int]
) -> Union[None, int]:
    # check if start or ending position is a wall
    if mat[start[0]][start[1]] is True or mat[start[0]][start[1]] is True:
        return None
    if len(mat) == 0 or len(mat[0]) == 0:
        return None  # invalid input matrix

    num_rows = len(mat)
    num_cols = len(mat[0])

    current = [start[0], start[1]]
    mat[current[0]][current[1]] = 0

    que = queue.Queue()
    que.put(current)

    while not que.empty():

        current = que.get()

        left = [current[0], current[1] - 1]
        right = [current[0], current[1] + 1]
        up = [current[0] + 1, current[1]]
        down = [current[0] - 1, current[1]]

        for move in [left, right, up, down]:

            # check whether current element is out of bounds
            if (
                move[0] > num_rows - 1
                or move[0] < 0
                or move[1] > num_cols - 1
                or move[1] < 0
            ):
                continue

            # if current element is wall (True) or we have already seen it (not False), skip
            if mat[move[0]][move[1]] is True or mat[move[0]][move[1]] is not False:
                continue

            # update current state, add one to where we came from
            mat[move[0]][move[1]] = mat[current[0]][current[1]] + 1

            # add to queue to later look at its neighbours
            que.put(move)

    # return value at end, or None if end is still unseen (could not reach it from anywhere)
    end_val = mat[end[0]][end[1]]
    if end_val is False:
        return None
    return end_val
