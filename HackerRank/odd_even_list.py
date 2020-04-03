

class Node(object):
    def __init__(self, _val):
        self.val = _val
        self.next = None

    def __str__(self):
        return str(self.val)


class List(object):
    def __init__(self, _head):
        self.head = _head

    def append(self, node):
        curr = self.head
        # traverse till the end
        while curr and curr.next:
            curr = curr.next
        curr.next = node

    def __str__(self):
        res = [self.head.val]
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return str(res)

    def odd_even_list(self):
        prev = None
        curr = self.head
        even_head = None
        even_curr = None
        while curr:
            if curr.val % 2:
                prev = curr
                curr = curr.next
            else:
                if prev:
                    if even_head:
                        prev.next = curr.next
                        even_curr.next = curr
                        even_curr = even_curr.next
                        even_curr.next = None
                        curr = prev.next
                    else:
                        prev.next = curr.next
                        even_head = curr
                        even_curr = curr
                        even_curr.next = None
                        curr = prev.next
                else:
                    if even_head:
                        even_curr.next = curr
                        even_curr = even_curr.next
                    else:
                        even_curr = even_head = curr
                    curr = curr.next
                    even_curr.next = None
                    self.head = curr

        if prev:
            prev.next = even_head
        else:
            self.head = even_head

    def reverse(self):
        curr = self.head

        def reverse_util(curr):
            if not curr.next:
                self.head = curr
                return curr
            res = reverse_util(curr.next)
            res.next = curr
            return curr
        res = reverse_util(curr)
        res.next = None

    def __reversed__(self):
        prev = None
        curr = self.head
        nxt = curr.next if curr else None
        while curr:
            curr.next = prev
            prev = curr
            curr = next
            nxt = curr.next if curr else None
        self.head = prev


if __name__ == '__main__':
    li = [2, 6, 3, 4, 1, 3, 5]
    li = [1, 3, 5]
    li = [2, 4, 6]
    li = [4, 1, 6]
    head = List(Node(li[0]))
    for i in li[1:]:
        head.append(Node(i))
    print(head)
    head.odd_even_list()
    print(head)
    head.reverse()
    print(head)
    head.__reversed__()
    print(head)
