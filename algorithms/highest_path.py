from typing import List


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
