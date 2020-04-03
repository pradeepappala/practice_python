

n, q = map(int, input().strip().split())

# create n communities with one each
a = [{i} for i in range(0, n+1)]

for _ in range(q):
    q_arr = input().strip().split()
    if q_arr[0] == 'M':
        c1 = int(q_arr[1])
        c2 = int(q_arr[2])
        a[c1] = a[c1].union(a[c2])
        a[c2] = a[c2].union(a[c1])
    elif q_arr[0] == 'Q':
        print(len(a[int(q_arr[1])]))

