import math
import os
import random
import re
import sys


def poisonous_plants(arr):
    s = []
    ss = []
    while arr:
        if not s or s[-1] <= arr[-1]:
            s.append(arr.pop())
        else:
            ss.append(s)
            s =[]
    if s:
        ss.append(s)

    days_count = 0
    while len(ss) > 1:
        print(ss)
        dp = [ss[i].pop() for i in range(len(ss) - 1)]
        ss = [ss[i] for i in range(len(ss)) if ss[i]]

        i = 0
        y = len(ss) - 1
        while i < y:
            if ss[i][-1] <= ss[i+1][0]:
                ss[i].extend(ss[i+1])
                del ss[i+1]
                y -= 1
                continue
            i += 1
        days_count += 1
    return days_count


if __name__ == '__main__':

    p = [6,5,8,4,7,6,10,9,8]

    p = [4,3,7,5,6,4,2]

    p = [4, 3, 7, 5, 6, 4, 2]

    p = [3, 2, 5, 4]

    p = [3, 1, 10, 7, 3, 5, 6, 6]

    p = [1, 1, 1, 1]

    p = [4, 3, 7, 5, 6, 4, 2]

    p = [6, 5, 8, 4, 7, 10, 9]

    p = [20, 5, 6, 15, 2, 2, 17, 2, 11, 5, 14, 5, 10, 9, 19, 12, 5]

    result = poisonous_plants(p)

    print(result)
