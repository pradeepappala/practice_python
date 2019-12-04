import numpy

n, m = map(int, input().strip().split())

arr = numpy.array([input().strip().split() for _ in range(n)], int)

print(numpy.sum(arr, axis=0))
print(numpy.round(numpy.prod(numpy.sum(arr, axis=0)), decimals=10))
