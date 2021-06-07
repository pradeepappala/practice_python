class Node:
    def __init__(self, _data):
        if isinstance(_data, list) or isinstance(_data, tuple):
            self.data = _data[0]
            self.next = None
        else:
            self.data = _data
            self.next = None
            return

        if isinstance(_data, list) or isinstance(_data, tuple):
            curr = self
            for i in _data[1:]:
                curr.next = Node(i)
                curr = curr.next

    def append_to_tail(self, _data):
        curr = self
        while(curr.next):
            curr = curr.next
        curr.next = Node(_data)

    def to_list(self):
        curr = self
        res = []
        while(curr.next):
            # print(curr.data)
            res.append(curr.data)
            curr = curr.next
        res.append(curr.data)
        # print(curr.data)
        return res

    def remove_dup(self):
        curr = self
        d = {}
        prev = None
        while curr:
            if d.get(curr.data):
                prev.next = prev.next.next
            else:
                d[curr.data] = True
                prev = curr
            curr = curr.next
        return self.to_list()

    def len_list(self):
        len_list = 0
        curr = self
        while(curr):
            len_list += 1
            curr = curr.next

        return len_list

    def ret_kth_last(self, k):
        if self.len_list() < k or k == 0:
            return -1

        if self.len_list() == k:
            return self.data

        kth_curr = self
        for i in range(k):
            kth_curr = kth_curr.next

        curr = self
        while(kth_curr):
            curr = curr.next
            kth_curr = kth_curr.next

        return curr.data


if __name__ == '__main__':
    head = Node(3)
    head.append_to_tail(4)
    print(head.to_list())