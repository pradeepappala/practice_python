import itertools

n = int(input().strip())
a = list(input().strip().split(' '))
k = int(input().strip())

res = [ bool('a' in i) for i in list(itertools.combinations(a, k))]

print(res.count(True)/len(res))