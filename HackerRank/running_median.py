import os
import sys


def running_median(a):
    res = []
    for i in range(len(a)):
        res = sorted_insert(res, a[i])
        if len(res) == 1:
            yield round(float(res[0]), 1)
        elif len(res) % 2 == 1:
            yield round(float(res[len(res)//2]), 1)
        else:
            yield round((res[len(res)//2-1] + res[len(res)//2])/2, 1)


def sorted_insert(res, x):
    for i in range(len(res)):
        if res[i] < x:
            continue
        res.insert(i, x)
        return res
    res.append(x)
    return res


def sorted_insert_a(a, l_index, h_index, x):
    if not a:
        return a.append(x)
    if l_index >= h_index:
        if l_index == 0:
            # insert at index 0 or 1
            return a.insert(0, x) if x <= a[l_index] else a.insert(1, x)
        elif h_index == len(a):
            # insert at end
            return a.insert(h_index, x) if x <= a[h_index] else a.append(x)
        else:
            # insert in middle
            return a.insert(l_index, x) if x <= a[l_index] else a.insert(l_index+1, x)

    m_index = (l_index + h_index)//2
    if x == a[m_index]:
        return a.insert(m_index, x)
    elif x < a[m_index]:
        h_index = m_index - 1
        return sorted_insert_a(a, l_index, h_index, x)
    else:
        l_index = m_index + 1
        return sorted_insert_a(a, l_index, h_index, x)


if __name__ == '__main__':

    a = []
    sorted_insert_a(a, 0, 0, 2)
    print(a)
    sorted_insert_a(a, 0, 0, 4)
    print(a)
    sorted_insert_a(a, 0, 1, 1)
    print(a)
    sorted_insert_a(a, 0, 2, 5)
    print(a)
    sorted_insert_a(a, 0, 3, 3)
    print(a)
    sorted_insert_a(a, 0, 4, 3)
    print(a)
    sorted_insert_a(a, 0, 5, 5)
    print(a)
    sorted_insert_a(a, 0, 6, 1)
    print(a)

    # result = running_median(a)

    # print('\n'.join(map(str, result)))
