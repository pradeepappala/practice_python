# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = 3, 2#map(int, input().split())
a = ['abc', 'def', 'ghi', 'abc']#[input() for i in range(n)]
#print(n, m, a)
for x in range(m):
    s = input()
    l = [str(i+1) for i in range(len(a)) if a[i] == s]
    print(' '.join(l)) if l else print(-1)