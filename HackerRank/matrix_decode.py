import re

n = 7
m = 3
matrix = [ 'Tsi',
           'h%x', 'i #',
           'sM ', '$a ',
           '#t%', 'ir!' ]

# Create two dimensional matrix
res = [list(i) for i in matrix]
# Join by column
res = ''.join([res[i][j] for j in range(m) for i in range(n)])
#print(res)
# Compile regular expression
print(re.sub(r'\b[^a-z0-9A-Z]+\b', ' ', res))
