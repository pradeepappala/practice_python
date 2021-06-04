def arrayRotation(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(i, N - i - 1):
            temp = arr[i][j]
            arr[i][j] = arr[N - j - 1][i]
            arr[N - j - 1][i] = arr[N - i - 1][N - j - 1]
            arr[N - i - 1][N - j - 1] = arr[j][N - i - 1]
            arr[j][N - i - 1] = temp
    return arr


def stringCompression(s1):
    cmpChar = s1[0]
    cnt = 0
    s2 = ''
    for c in s1:
        if c == cmpChar:
            cnt += 1
            continue
        s2 += cmpChar + str(cnt)
        cmpChar = c
        cnt = 1
    s2 += cmpChar + str(cnt)
    return s1 if len(s1) < len(s2) else s2


def oneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    awayCount = 0
    if len(s1) == len(s2):
        for i, c in enumerate(s1):
            if s2[i] != c:
                awayCount += 1
        return True if awayCount <= 1 else False

    correctionIndex = 0
    # take largest string in to s1
    s1, s2 = (s2, s1) if len(s1) < len(s2) else (s1, s2)
    for i, c in enumerate(s1):
        if i == len(s1) - 1 and correctionIndex == 0:
            awayCount += 1
            continue

        if s2[i - correctionIndex] != c:
            correctionIndex = 1
            awayCount += 1
    else:
        return True if awayCount <= 1 else False


def palinPerm(s):
    s = s.lower()
    d = {}
    for c in s:
        if c == ' ':
            continue

        d[c] = d.get(c, 0) + 1

    return True if len(list(filter(lambda x: x % 2, d.values()))) <= 1 else False
