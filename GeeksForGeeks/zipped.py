n,m = map(int, input().split())
res = [(list(map(float, input().split()))) for i in range(m)]
for x in list(zip(*res)):
    print(sum(x)/m)

