import unittest
from CrackingCodingInterview.linked_list import Node


class TestLinkedList(unittest.TestCase):
    def test_create_head(self):
        res = Node(3)
        self.assertEqual([3], res.to_list())
        input = [3, 4, 5, 1]
        res = Node(input)
        self.assertEqual(input, res.to_list())

    def test_append_to_tail(self):
        res = Node(3)
        self.assertEqual([3], res.to_list())
        res.append_to_tail(1)
        self.assertEqual([3, 1], res.to_list())

    def test_remove_dup(self):
        input = [3, 4, 5, 1, 5, 1, 4, 3]
        res = Node(input)
        expected = [3, 4, 5, 1]
        self.assertEqual(expected, res.remove_dup())
        input = [3, 3, 3, 3, 3]
        res = Node(input)
        expected = [3]
        self.assertEqual(expected, res.remove_dup())
        input = [3, 2, 1, 5, 4]
        res = Node(input)
        self.assertEqual(input, res.remove_dup())

    def test_kth_last_elem(self):
        input = [1, 5, 1, 4, 3]
        res = Node(input)
        self.assertEqual(-1, res.ret_kth_last(8))
        self.assertEqual(-1, res.ret_kth_last(0))
        self.assertEqual(1, res.ret_kth_last(5))
        self.assertEqual(3, res.ret_kth_last(1))
        self.assertEqual(1, res.ret_kth_last(3))


if __name__ == '__main__':
    unittest.main()