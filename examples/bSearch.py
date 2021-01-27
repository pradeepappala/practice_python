def bSearch_mod(a, k):
    if not a:
        return -1

    if a[len(a)//2] == k:
        return len(a)//2

    if a[len(a)//2] < k:
        import math
        return math.ceil(len(a)/2) + bSearch(a[len(a)//2+1:], k)

    return bSearch(a[:len(a)//2], k)


def bSearch(a, l, h, k):
    if not a or l > h:
        return -1

    m = (l + h)//2

    if a[m] == k:
        return m

    if a[m] < k:
        return bSearch(a, m+1, h, k)

    return bSearch(a, l, m - 1, k)


def myHeapify(a, i):
    c1i = (i+1)*2-1
    c2i = (i+1)*2
    v1 = v2 = None
    if c1i < len(a):
        v1 = a[c1i]
    if c2i < len(a):
        v2 = a[c2i]

    if not v1 and not v2:
        return  # leaf node

    if v1 and not v2:
        if v1 <= a[i]:
            return  # already heap
        a[c1i], a[i] = a[i], a[c1i]
        return  # heap is a complete binary tree, this case occurs only once and no need to proceed further

    if v1 <= a[i] and v2 <= a[i]:
        return  # already heap

    if v1 < v2:
        a[c2i], a[i] = a[i], a[c2i]
        return myHeapify(a, c2i)  # swap and run heapify on child

    a[c1i], a[i] = a[i], a[c1i]
    return myHeapify(a, c1i)  # swap and run heapify on child


def mergeSort(a, l, h):
    if l >= h:
        return

    m = (l + h) // 2
    mergeSort(a, l, m)
    mergeSort(a, m+1, h)
    merge(a, l, m, h)


def merge(a, l, m, h):
    res = [-1] * (h -l + 1)
    k = 0
    i = l
    j = m + 1
    while i <= m and j <= h:
        if a[i] <= a[j]:
            res[k] = a[i]
            i += 1
            k += 1
        else:
            res[k] = a[j]
            j += 1
            k += 1

    if i <= m:
        for v in a[i:m+1]:
            res[k] = v
            k += 1

    if j <= h:
        for v in a[j:h+1]:
            res[k] = v
            k += 1

    a[l:h+1] = res


if __name__ == '__main__':
    print(bSearch([1, 2, 3, 4], 0, 4, 1))
    print(bSearch([1, 2, 3, 4], 0, 4, 2))
    print(bSearch([1, 2, 3, 4], 0, 4, 3))
    print(bSearch([1, 2, 3, 4], 0, 4, 4))
    print(bSearch([1, 2, 3, 4, 5], 0, 5, 4))
    print(bSearch([1, 2, 3, 4, 5], 0, 5, 5))
    a = [1, 2, 3, 4, 5, 6]
    print(a)
    for i in range(len(a), 0, -1):
        myHeapify(a, i - 1)
        print(f'After heapify at {i - 1} is {a}')
    print(a)

    a = [5, 2, 3, 1, 4]
    c = [-1] * len(a)
    merge(a, 1, 2, 4)
    print(c)
    print(a)

    a = [3, 2, 1]
    c = [-1] * len(a)
    mergeSort(a, 0, len(a) - 1)
    print(c)
    print(a)

