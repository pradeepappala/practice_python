#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(board):
    # return no it board is empty
    if not board:
        return 'No'

    # check each row first elem with next row first elem is valid
    res = [board[i][0] != board[i + 1][0] for i in range(len(board[0]) - 1)]
    if False in res:
        return 'No'

    # check elem's in each row is valid
    for i in range(len(board[0])):
        res = [board[i][j] != board[i][j + 1] for j in range(len(board[0]) - 1)]
        if False in res:
            return 'No'

    # return true
    return 'Yes'


if __name__ == '__main__':

    # t = int(input().strip())
    t = 1

    for t_itr in range(t):
        '''
        n = int(input().strip())

        board = []

        for _ in range(n):
            board.append(list(map(int, input().rstrip().split())))
        '''
        n = 2
        board = [[0,0], [0,0]]
        #board = [[0,1], [1,0]]

        result = solve(board)

        print(result + '\n')
