import itertools

# Read k, m
k, m = map(int, input().strip().split(' '))


def square_sum(t):
    return sum([i*i for i in t]) % m


a = max(list(map(lambda t : sum([i*i for i in t]) % m, list(itertools.product(*[list(map(int, input().strip().split(' ')))[1:] for i in range(k)])))))
print(a)
