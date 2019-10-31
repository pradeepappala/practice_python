'''
#set mutations

_ = int(input())
a = set(map(int, input().split()))
for _ in range(int(input())):
    s,i = input().split()
    b = set(map(int, input().split()))
    eval('a.'+s+'('+'b'+')')
print(sum(a))
'''
#strict super set
setA = set(map(int, input().split()))
n = int(input())
res = []
for i in range(n):
    tempSet = set(map(int, input().split()))
    res.append(True) if setA.difference(tempSet) and not tempSet.difference(setA) else res.append(False)

print(all(res))
