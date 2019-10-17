from itertools import combinations

s, k = 'HACK', 2 #map(str, input().split(' '))
k = int(k)
[[print(''.join(i)) for i in combinations(sorted(s), i)] for i in range(1, k+1)]

print('-----------------')

from itertools import combinations_with_replacement

s, k = 'HACK', 2 #map(str, input().split(' '))
k = int(k)
[print(''.join(k)) for k in combinations_with_replacement(sorted(s), k)]

print('-----------------')

from itertools import groupby

s = '1222311' #input()

l =[]
for k, g in groupby(s):
    #print(len(list(g)), k)
    l.append(str((len(list(g)), int(k))))

print(''.join(l))

print('-----------------')

print(' '.join([str((len(list(g)), int(k))) for k, g in groupby(s)]))
