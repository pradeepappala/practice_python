import os
import sys
import math


# Complete the solve function below.
def solve(arr, queries):
    for d in queries:
        res = math.inf
        for i in range(len(arr)+1-d):
            res = min(res, max(arr[i:i+d]))
        yield res


if __name__ == '__main__':

    arr = [33, 11, 44, 11, 55]

    queries = [1, 2, 3, 4, 5]

    result = solve(arr, queries)

    print('\n'.join(map(str, result)))
