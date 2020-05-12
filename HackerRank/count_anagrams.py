import math
import os
import random
import re
import sys

'''
def isAnagrams(a, b):
    d_a = dict()
    d_b = dict()
    for i in a:
        d_a[i] = d_a.get(i, 0) + 1

    for i in b:
        d_b[i] = d_b.get(i, 0) + 1

    if len(d_a.items()) != len(d_b.items()):
        return False

    for k, v in d_a.items():
        if v != d_b.get(k, 0):
            return False

    return True


def sherlockAndAnagrams(s):
    res = 0
    for w in range(1, len(s)):
        for i in range(0, len(s) - w):
            for j in range(i + 1, len(s) - w + 1):
                if isAnagrams(s[i:i + w], s[j:j + w]):
                    res += 1

    return res
'''

from collections import Counter


def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        for j in b:
            count += b[j]*(b[j]-1)/2
    return int(count)


if __name__ == '__main__':
    s = 'ifailuhkqq'

    result = sherlockAndAnagrams(s)

    print(result)

