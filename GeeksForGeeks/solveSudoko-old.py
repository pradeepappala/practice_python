import pprint


def solve_sudoko(a):
    # get values in row, col and 3x3 matrix
    rP = [[a[i][j] for j in range(9) if a[i][j] != 0] for i in range(9)]
    cP = [[a[i][j] for i in range(9) if a[i][j] != 0] for j in range(9)]
    tP = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            if a[i][j] != 0:
                tP[i//3*3 + j//3].append(a[i][j])

    # get possible values in row, col and 3x3 matrix
    rP = [[x for x in range(1,10) if x not in rP[i]] for i in range(9)]
    cP = [[x for x in range(1,10) if x not in cP[i]] for i in range(9)]
    tP = [[x for x in range(1,10) if x not in tP[i]] for i in range(9)]

    stop_iteration = 1
    # iterate while at least one changed
    while stop_iteration :
        stop_iteration = 0
        for i in range(9):
            for j in range(9):
                flag = 0
                if a[i][j] == 0:
                    if len(rP[i]) == 1:
                        a[i][j] = rP[i][0]
                        flag = 1
                    elif len(cP[j]) == 1:
                        a[i][j] = cP[j][0]
                        flag = 1
                    elif len(tP[i//3*3+j//3]) == 1:
                        a[i][j] = tP[i//3*3+j//3][0]
                        flag = 1
                    else:
                        # Find intersection of all three possibilities for this i,j
                        inter_section = set(rP[i]).intersection(set(cP[j]), set(tP[i//3*3+j//3]))
                        if(len(inter_section) == 1):
                            a[i][j] = inter_section.pop()
                            flag = 1
                if flag:
                    try:
                        stop_iteration = 1
                        rP[i].remove(a[i][j])
                        cP[j].remove(a[i][j])
                        tP[i//3*3+j//3].remove(a[i][j])
                    except Exception as e:
                        print('caught exception!!!', e)
    return a


def main():
    '''
    a = [[7, 0, 3, 4, 5, 0, 9, 0, 6],
         [0, 6, 0, 0, 3, 0, 0, 0, 0],
         [0, 0, 0, 9, 0, 0, 0, 7, 2],
         [0, 0, 1, 0, 7, 8, 0, 4, 9],
         [0, 7, 8, 0, 0, 0, 1, 6, 0],
         [4, 2, 0, 1, 9, 0, 8, 0, 0],
         [3, 8, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 6, 0, 0, 3, 0],
         [6, 0, 5, 0, 8, 4, 7, 0, 1]]
    '''

    a = [[0, 9, 4, 0, 5, 3, 1, 0, 0],
         [2, 0, 0, 0, 1, 7, 0, 0, 0],
         [0, 3, 0, 8, 0, 0, 5, 4, 0],
         [0, 6, 8, 9, 0, 0, 0, 7, 0],
         [4, 7, 0, 0, 8, 0, 0, 9, 5],
         [0, 2, 0, 0, 0, 5, 4, 8, 0],
         [0, 8, 5, 0, 0, 9, 0, 1, 0],
         [0, 0, 0, 1, 7, 0, 0, 0, 9],
         [0, 0, 9, 5, 2, 0, 3, 6, 0]]

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(solve_sudoko(a))


if __name__ == '__main__':
    main()
