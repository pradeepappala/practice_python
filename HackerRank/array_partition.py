import math
import os
import random
import re
import sys
import itertools
from functools import reduce


def prod(x, y):
    return x*y

# Complete the solve function below.
def solve(a):
    b = set(a)
    res = []
    for i in range(1, len(b)):
        for j in itertools.combinations(b, i):
            res.append((set(j), b.difference(j)))

    count = 0
    for i in range(len(res)):
        if math.gcd(reduce(prod, res[i][0]), reduce(prod, res[i][1])) == 1:
            count += 1

    return count


if __name__ == '__main__':

    # t = int(input().strip())
    t = 1

    for t_itr in range(t):
        '''
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))
        '''
        # 10
        # 5 7 5 2 13 13 13 2 5 5
        # 14
        # 5 7 5 13 11 7 3 2 2 11 13 13 3 5
        a_count = 12
        a = [1, 11, 4, 13, 8, 6, 6, 15, 14, 1, 5, 9]

        result = solve(a)

        print(str(result) + '\n')
