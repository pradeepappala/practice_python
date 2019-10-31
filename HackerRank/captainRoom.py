# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
l = list(map(int, input().split()))
print([i for i in l if l.count(i) == 1][0])
