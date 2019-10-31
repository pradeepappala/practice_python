def print_rangoli(size):
    # your code goes here
    width = (size - 1) * 4 + 1
    res = ''.join([chr(ord('a')+i) for i in range(size)])
    print(res)
    for i in range(size):
        temp = res[:-i-2:-1] + res[size-i:]
        print('-'.join(temp).center(width, '-'))
    for i in range(size-1):
        j = size-1-i-1
        temp = res[:-j-2:-1] + res[size-j:]
        print('-'.join(temp).center(width, '-'))


if __name__ == '__main__':
    n = 3 # int(input())
    print_rangoli(n)