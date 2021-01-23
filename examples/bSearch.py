def bSearch(a, k):
    if not a:
        return False

    if a[len(a)//2] == k:
        return True

    if a[len(a)//2] < k:
        return bSearch(a[len(a)//2+1:], k)

    return bSearch(a[:len(a)//2], k)