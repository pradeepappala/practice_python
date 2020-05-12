import math
import os
import random
import re
import sys

# Complete the gridlandMetro function below.
def gridlandMetro(n, m, k, track):
    res = [[0 for j in range(m)] for i in range(n)]
    for i in range(k):
        r, s, e = track[i]
        if s == e:
            continue
        if s > e:
            for j in range(s-1, e-1, -1):
                res[r-1][j] = 1
        else:
            for j in range(s-1, e):
                res[r-1][j] = 1

    print(res)
    res_sum = 0
    for i in range(n):
        res_sum += res[i].count(0)
    return res_sum


if __name__ == '__main__':
    # nmk = input().split()
    # n = int(nmk[0])
    # m = int(nmk[1])
    # k = int(nmk[2])
    # track = []
    # for _ in range(k):
    #     track.append(list(map(int, input().rstrip().split())))

    n = m = k = 4
    track = [[4, 4, 3], [2, 2, 3], [3, 1, 4], [4, 4, 4]]
    result = gridlandMetro(n, m, k, track)
    print(result)

