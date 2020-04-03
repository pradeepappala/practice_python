class FindStr(object):
    neighbour_list = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    def __init__(self, _arr_2d, _search_str):
        self.arr_2d = _arr_2d
        self.search_str = _search_str
        self.visited = [[False for i in range(len(self.arr_2d[0]))] for j in range(len(self.arr_2d))]

    def find_str(self):
        if not self.arr_2d or not self.search_str:
            return False

        for i in range(len(self.arr_2d)):
            for j in range(len(self.arr_2d[0])):
                self.visited = [[False for i in range(len(self.arr_2d[0]))] for j in range(len(self.arr_2d))]
                if self._find_util(i, j, 0):
                    return True
        return False

    def _is_valid(self, i, j):
        if i < 0 or i >= len(self.arr_2d):
            return False

        if j < 0 or j >= len(self.arr_2d[0]):
            return False

        if self.visited[i][j]:
            return False

        return True

    def _find_util(self, i, j, index):
        if not self._is_valid(i, j):
            return False

        if a[i][j] != self.search_str[index]:
            return False

        if index == len(self.search_str)-1:
            return True

        self.visited[i][j] = True

        for k in self.neighbour_list:
            if self._find_util(i+k[0], j+k[1], index+1):
                return True

        self.visited[i][j] = False
        return False


if __name__ == '__main__':
    a = [['a', 'b', 'c'],
         ['c', 'd', 'e'],
         ['e', 'f', 'g'],
         ['g', 'h', 'i'],
         ['i', 'j', 'k']]

    obj = FindStr(a, 'adehijk')
    print(obj.find_str())
