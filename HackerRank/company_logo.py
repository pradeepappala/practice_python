


if __name__ == '__main__' :
    # s = input()
    s = 'aabbbccde'
    a = [0 for _ in range(26)]
    for i in range(ord('a'), ord('z')+1):
        a[i-ord('a')] = s.count(chr(i))

    for _ in range(3):
        m = max(a)
        i = a.index(m)
        print(chr(i+ord('a')), m)
        a[i] = 0
