import re
n = 1 # int(input())
for i in range(n):
    s = 'abc #1abcde cdef #123'#input()
    m = re.findall(r'^(?!#).*#[-1-9ABCDEF]{3,6}', s, re.I)
    if m:
        print(m[0], type(m))
        print(re.findall('#[0-9ABCDEF]{3,6}', m[0], re.I))

print(*[[re.findall('#[0-9ABCDEF]{3,6}', x, re.I) for x in re.findall(r'^(?!#).*#[-1-9ABCDEF]{3,6}', input(), re.I)] for _ in range(n)][0][0], sep='\n')