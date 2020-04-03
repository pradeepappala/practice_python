#!/bin/python3

import os
import sys
import math


# Complete the solve function below.
def solve(arr, queries):
    for d in queries:
        res = curr_max = max(arr[0:d])
        mod_arr = [curr_max]
        for i in range(1, len(arr)-d+1):
            if arr[i+d-1] > curr_max:
                curr_max = arr[i+d-1]
                mod_arr.append(curr_max)
            elif arr[i-1] < curr_max:
                mod_arr.append(curr_max)
                continue
            else:
                curr_max = max(arr[i:i+d])
                mod_arr.append(curr_max)

        res = min(mod_arr)
        yield res


if __name__ == '__main__':

    arr = [33, 11, 44, 11, 55]
    queries = [1,2,3]
    result = solve(arr, queries)

    print('\n'.join(map(str, result)))
