

def oneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    awayCount = 0
    if len(s1) == len(s2):
        for i, c in enumerate(s1):
            if s2[i] != c:
                awayCount += 1
        else:
            return True if awayCount <=1 else False

    correctionIndex = 0
    # take largest string in to s1
    s1, s2 = (s2, s1) if len(s1) < len(s2) else (s1, s2)
    for i, c in enumerate(s1):
        if i == len(s1) - 1 and correctionIndex == 0:
            awayCount += 1
            continue

        if s2[i-correctionIndex] != c:
            correctionIndex = 1
            awayCount += 1
    else:
        return True if awayCount <=1 else False


def palinPerm(s):
    s = s.lower()
    d = {}
    for c in s:
        if c == ' ':
            continue

        d[c] = d.get(c, 0) + 1

    return True if len(list(filter(lambda x: x%2, d.values()))) <= 1 else False
