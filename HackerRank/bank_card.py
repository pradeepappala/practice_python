# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def is_valid(card_num):
    p = re.compile(r'^(?!.*(\d)(-?\1){3})[4-6]\d{3}(-?\d{4}){3}$')
    return bool(p.search(card_num))

if __name__ == '__main__':
    n = int(input())

    p = re.compile(r'^(?!.*(\d)(-?\1){3})[4-6]\d{3}(-?\d{4}){3}$')
    print(*['Valid' if p.search(input().strip()) else 'Invalid' for i in range(n)])
