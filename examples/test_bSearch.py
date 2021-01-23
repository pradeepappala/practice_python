import unittest
import bSearch


class Test_bSearch(unittest.TestCase):
    def test_founds(self):
        self.assertTrue(bSearch.bSearch([1, 2, 3], 1))
        self.assertTrue(bSearch.bSearch([1, 2, 3], 2))
        self.assertTrue(bSearch.bSearch([1, 2, 3], 3))
        self.assertTrue(bSearch.bSearch([1, 2, 3, 4], 2))
        self.assertTrue(bSearch.bSearch([1, 2, 3, 4, 5, 6, 7], 5))

    def test_notfound(self):
        self.assertFalse(bSearch.bSearch([1, 2, 3], 4))


if __name__ == '__main__':
    unittest.main()
