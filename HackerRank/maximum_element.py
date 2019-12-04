# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())

s = []
curr_max_index = 0

for _ in range(n):
    inp = list(map(int, input().strip().split()))
    if inp[0] == 1:
        if len(s) == 0:
            curr_max_index = 0
            s.append((inp[1], curr_max_index))
        elif s[curr_max_index][0] > inp[1]:
            s.append((inp[1], s[curr_max_index][1]))
        else:
            curr_max_index = len(s)
            s.append((inp[1], curr_max_index))
    elif inp[0] == 2 and len(s):
        t = s.pop()
        curr_max_index = s[-1][1] if len(s) else 0
    elif inp[0] == 3 and len(s):
        t = s[-1]
        print(s[t[1]][0])
