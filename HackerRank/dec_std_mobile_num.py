def wrapper(f):
    def fun(l):
        import re
        # return f(['+91 ' + i[:5] + ' ' + i[5:] for i in [re.sub('.*(\d{10}$)', '\\1', i, )for i in l]])
        return f(['+91 {} {}'.format(i[:5], i[5:]) for i in [re.sub('.*(\d{10}$)', '\\1', i, ) for i in l]])
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    # l = [input() for _ in range(int(input()))]
    in_list = ['09000058059', '919000058058' ]
    sort_phone(in_list)