#M = 3; N = 6; P = 4; Q = 6
#print(M, N, P, Q)
#print([ (l, b) for l in range(M, N+1) for b in range(P, Q+1)])
#print([ ((l, b), countPerBar(l, b)) for l in range(M, N+1) for b in range(P, Q+1)])

def countPerBar(l, b):
    if not l or not b:
        return 0
    if l == b:
        return 1
    return countPerBar(max(l,b) - min(l,b), min(l,b)) + 1

M = int(input())
N = int(input())
P = int(input())
Q = int(input())
print(M, N, P, Q)
print('Total Count : {res}'.format(res=sum([countPerBar(l, b) for l in range(M, N+1) for b in range(P, Q+1)])))
