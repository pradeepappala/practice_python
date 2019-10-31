import re

s = 'aaadaa'
p = re.compile('aa')
i = 0
while i < len(s):
    m = p.search(s, i)
    if m:
        print((m.start(), m.end()))
        i = m.start() + 1
