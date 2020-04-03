

def print_formatted(number):
    # your code goes here
    width = len(bin(n)) - 2
    for i in range(1, n+1):
        print(str(i).rjust(width), oct(i)[2:].rjust(width), str(hex(i).upper())[2:].rjust(width), bin(i)[2:].rjust(width))

if __name__ == '__main__':
    n = 10 #int(input())
    a = [9, 2, 3, 6, 5, 4, 3, 2, 2, 2]
    for i, x in enumerate(a[-2::-1]):
        print(i, x, a[len(a) - i])
    print_formatted(n)




