import unittest
import bSearch


class Test_bSearch(unittest.TestCase):
    def test_founds(self):
        self.assertEqual(bSearch.bSearch([1, 2, 3], 0, 2, 1), 0)
        self.assertEqual(bSearch.bSearch([1, 2, 3], 0, 2, 2), 1)
        self.assertEqual(bSearch.bSearch([1, 2, 3], 0, 2, 3), 2)
        self.assertEqual(bSearch.bSearch([1, 2, 3, 4], 0, 3, 2), 1)
        self.assertEqual(bSearch.bSearch([1, 2, 3, 4, 5, 6, 7], 0, 6, 5), 4)

    def test_notfound(self):
        self.assertEqual(bSearch.bSearch([1, 2, 3], 0, 2, 4), -1)
        self.assertEqual(bSearch.bSearch([], 0, 0, 4), -1)


class Test_myHeapify(unittest.TestCase):
    def test_my_heapify(self):
        a = [1, 2, 3, 4, 5]
        bSearch.myHeapify(a, 4)
        self.assertEqual(a, [1, 2, 3, 4, 5])
        bSearch.myHeapify(a, 1)
        self.assertEqual(a, [1, 5, 3, 4, 2])
        a = [1, 2, 3, 4, 5]


class Test_merge(unittest.TestCase):
    def setUp(self):
        self.a = [2, 1, 3, 4, 5]

    def test_merge(self):
        bSearch.merge(self.a, 0, 0, 1)
        self.assertEqual(self.a, [1, 2, 3, 4, 5])

    def test_mergeSort(self):
        bSearch.mergeSort(self.a, 0, len(self.a) - 1)
        self.assertEqual(self.a, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
