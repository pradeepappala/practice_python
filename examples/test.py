# N = int(input())
# l = list(map(int, input().split(' ')))
# l = [1,2,4,3,3]
l = [2,2,2,2,2,2,2]
l_l = [[],[],[],[]]
for i in l:
    l_l[i-1].append(i)
# length of 4's list
res = len(l_l[3]) + len(l_l[2])
# common length from 3's and 1's list
min_3_1 = min(len(l_l[2]), len(l_l[0]))
l_l[0] = [] if len(l_l[3]) > len(l_l[0]) else l_l[0][min_3_1:]
import math
if not l_l[0]:
    res += math.ceil(len(l_l[1])/2)
elif not l_l[1]:
    res += math.ceil(len(l_l[0])/4)
else:
    min_2_1 = min(len(l_l[1]), len(l_l[0])*2)
    res += min_2_1
    l_l[1] = l_l[1][min_2_1:]
    l_l[0] = [] if len(l_l[0]) < min_2_1 else l_l[0][min_2_1*2:]
    if not l_l[0]:
        res += math.ceil(len(l_l[1])/2)
    elif not l_l[1]:
        res += math.ceil(len(l_l[0])/4)
print(res)

