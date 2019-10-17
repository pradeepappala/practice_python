l = ['ABC123DEFG', 'BCDEF12344', 'DEFG123', 'abc-123456', 'ABCDEFGHI1', '12345678ab', '123ABcdefg']
import re
from collections import Counter
p = re.compile('[a-zA-Z0-9]*')
q = re.compile('[A-Z]')
r = re.compile('[0-9]')

for i in range(len(l)):
    print('Valid' if len(l[i]) == 10 and Counter(l[i]).most_common(1)[0][1] == 1 and p.fullmatch(l[i]) and len(q.findall(l[i])) >= 2 and len(r.findall(l[i])) >= 3 else 'Invalid')

