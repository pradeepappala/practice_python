import math
import os
import random
import re
import sys

#
# Complete the 'get_ways' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
res_lists = set()


def get_ways(n, c):
    res_count_list = [-1 for i in range(n)]

    def get_ways_util(x, y, stack_l=None):
        if not stack_l:
            stack_l = []
        if x < 0:
            return 0
        if x == 0:
            print('stack_l', sorted(stack_l))
            if tuple(sorted(stack_l)) in res_lists:
                return 0
            res_lists.add(tuple(sorted(stack_l)))
            return 1
        if res_count_list[x-1] != -1:
            print(x)
            return res_count_list[x-1]
        res_sum = 0
        for i in y:
            stack_l.append(i)
            res_sum += get_ways_util(x - i, y, stack_l)
            stack_l.pop()
        res_count_list[x-1] = res_sum
        return res_sum
    res = get_ways_util(n, c)
    print(res_lists)
    return res


if __name__ == '__main__':
    n = 4
    c = [1, 2, 3]

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = get_ways(n, c)

    print(str(ways) + '\n')
