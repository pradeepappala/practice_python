# Complete the solve function below.
def solve(s):
    return ' '.join([ i.capitalize() for i in s.split(' ') ])

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = 'pradeep appala' #input()

    print(solve(s))

    #fptr.write(result + '\n')

    #fptr.close()