from collections import namedtuple
n = int(input())
Table = namedtuple('Table', ','.join(input().split()))
print(sum([int(Table(*input().split()).MARKS) for i in range(n)])/n)

import calendar

print(calendar.day_name[calendar.weekday(2019, 8, 10)])