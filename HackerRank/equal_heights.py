#!/bin/python3

import os
import sys


#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    # find sum of stacks
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)

    # while any of the list is not null
    while (h1 and h2 and h3):

        # if stacks are equal return
        if s1 == s2 == s3:
            return s1

        # remove one element from max stack
        m = max(s1, s2, s3)
        if s1 == m:
            s1 -= h1.pop(0)
        if s2 == m:
            s2 -= h2.pop(0)
        if s3 == m:
            s3 -= h3.pop(0)

    return 0


if __name__ == '__main__':

    '''
    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))
    '''

    h1 = [3, 2, 1, 1, 1]
    h2 = [4, 3, 2]
    h3 = [1, 1, 4, 1]
    result = equalStacks(h1, h2, h3)

    print(str(result) + '\n')
