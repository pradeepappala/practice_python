import os
import sys


#
# Complete the twoStacks function below.
#
def two_stacks(x, a, b):
    res_score = 0
    res_sum = 0
    # till a and b is not empty
    while res_sum < x and a and b:
        m = min(a[0], b[0])
        res_sum += m
        if res_sum > x:
            return res_score
        res_score += 1
        a.pop(0) if m == a[0] else b.pop(0)

    # either a or b is empty
    a = a or b
    while res_sum < x and a:
        res_sum += a[0]
        if res_sum > x:
            return res_score
        res_score += 1
        a.pop(0)

    return res_score


if __name__ == '__main__':

    # g = int(input())
    g = 1

    for g_itr in range(g):
        # nmx = input().split()

        # n = int(nmx[0])

        # m = int(nmx[1])

        # x = int(nmx[2])

        # a = list(map(int, input().rstrip().split()))

        # b = list(map(int, input().rstrip().split()))

        result = two_stacks(10, [4, 2, 4, 6, 1], [2, 1, 8, 5])

        print(str(result) + '\n')
