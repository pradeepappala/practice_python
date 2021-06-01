import os
import sys
import math


def isPrime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 4
    while i < (math.ceil(n / 2) + 1):
        if n % i == 0 or n % (i + 5) == 0:
            return False
        i = i + 6

    return True


#
# Complete the sillyGame function below.
#
def sillyGame(n):
    #
    # Write your code here.
    #
    totalPrimes = 0
    for i in range(1, n + 1):
        if isPrime(i):
            totalPrimes += 1

    return 'Alice' if totalPrimes % 2 else 'Bob'


if __name__ == '__main__':

    # g = int(input())
    g = [ 1, 2, 5 ]

    for n in g:
        result = sillyGame(n)
        print(result)

