#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    # to check final index
    ind = 0
    res = []
    for i in range(len(s)):
        if s[i] in '{[(':
            res.append(s[i])
        else:
            # return 'No' if res is empty
            if not len(res):
                break
            temp = res.pop()
            if ((s[i] == '}' and temp == '{')
                or (s[i] == ']' and temp == '[')
                or (s[i] == ')' and temp == '(')):
                ind = i
                # process next index
                continue
            break
    return 'Yes' if(ind == len(s)-1 and not len(res)) else 'No'


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result + '\n')
