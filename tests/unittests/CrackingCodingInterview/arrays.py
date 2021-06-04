import unittest
from CrackingCodingInterview.arrays import palinPerm
from CrackingCodingInterview.arrays import oneAway
from CrackingCodingInterview.arrays import stringCompression
from CrackingCodingInterview.arrays import arrayRotation


class TestPalinPerm(unittest.TestCase):
    def test_palinPerm_Fail(self):
        self.assertEqual(False, palinPerm('abc def'))
        self.assertEqual(False, palinPerm('abc     def'))

    def test_palinPerm_Success(self):
        self.assertTrue(palinPerm('aba dd'))
        self.assertTrue(palinPerm('aba      dd'))
        self.assertTrue(palinPerm('aba      Dd'))

    def test_oneAway_Fail(self):
        self.assertEqual(False, oneAway('paleee', 'bake'))
        self.assertEqual(False, oneAway('pale', 'bake'))
        self.assertEqual(False, oneAway('pal', 'pake'))
        self.assertEqual(False, oneAway('pales', 'bake'))

    def test_oneAway_Pass(self):
        self.assertTrue(oneAway('pale', 'pake'))
        self.assertTrue(oneAway('pale', 'pal'))
        self.assertTrue(oneAway('pale', 'pales'))

    def test_stringCompression(self):
        # uncompress
        self.assertEqual(stringCompression('abc'), 'abc')
        # compressed
        self.assertEqual(stringCompression('aabb'), 'a2b2')
        self.assertEqual(stringCompression('aaabbb'), 'a3b3')

    def test_arrayRotation(self):
        self.assertEqual(arrayRotation([[1,2], [3,4]]), [[3, 1], [4, 2]])
        array = [[i*3+j+1 for j in range(3)] for i in range(3)]
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], arrayRotation(array))
        array = [[i*4+j+1 for j in range(4)] for i in range(4)]
        self.assertEqual([[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]], arrayRotation(array))


if __name__ == '__main__':
    unittest.main()
