import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))

import re

def replaceAndOr(match):
    if match.group(0) == ' && ':
        return ' and '
    elif match.group(0) == ' || ':
        return ' or '

n = int(input())
for _ in range(n):
    s = re.sub(r'\s+([&\|]{2})\s+', replaceAndOr , input())
    print(re.sub(r'\s+([&\|]{2})\s+', replaceAndOr , s))