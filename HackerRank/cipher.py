import math
import os
import random
import re
import sys


# Complete the cipher function below.
def cipher(k, s):
    s = list(map(int, list(s)))
    n = len(s) - k + 1
    res = []
    for i in range(n):
        if i == 0:
            res.append(s[i])
        elif i < k:
            res.append(s[i-1]^s[i])
        else:
            res.append(s[i-1]^res[i-k]^s[i])
    return ''.join(map(str, res))


if __name__ == '__main__':

    n = 5

    k = 4

    s = '11000011'

    result = cipher(k, s)

    print(result + '\n')

