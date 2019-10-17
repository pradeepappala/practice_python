

def print_formatted(number):
    # your code goes here
    width = len(bin(n)) - 2
    for i in range(1, n+1):
        print(str(i).rjust(width), oct(i)[2:].rjust(width), str(hex(i).upper())[2:].rjust(width), bin(i)[2:].rjust(width))

if __name__ == '__main__':
    n = 10 #int(input())
    print_formatted(n)




