import math
import os
import random
import re
import sys


# Complete the poisonous_plants function below.
def poisonous_plants(p):
    s = list()
    # initialize stack and prev to first elem
    s.append(p[0])
    prev = s[-1]
    count = 0
    res = 0
    for i in p[1:]:
        if i > prev:
            # reset count to one
            count = 1
        elif i > s[-1]:
            # incr count by one
            count += 1
        else:
            # reset count to zero
            count = 0
        res = max(res, count)
        prev = i
    return res


if __name__ == '__main__':

    p = [6,5,8,4,7,6,10,9,8]

    p = [4,3,7,5,6,4,2]
    result = poisonous_plants(p)

    print(result)
