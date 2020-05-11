import numpy as np


def approximate_pi(num_samples: int):

    in_circle = 0
    for ii in range(num_samples):
        r1 = np.random.uniform(0, 1)
        r2 = np.random.uniform(0, 1)

        if r1 ** 2 + r2 ** 2 <= 1:
            in_circle += 1

    proportion_in_circle = in_circle / num_samples
    return 4 * proportion_in_circle


if __name__ == "__main__":

    approx = approximate_pi(int(1e7))
    print("Approximation to pi: ", approx)
