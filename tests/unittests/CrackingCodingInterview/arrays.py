import unittest
from CrackingCodingInterview.arrays import palinPerm
from CrackingCodingInterview.arrays import oneAway
from CrackingCodingInterview.arrays import stringCompression


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
        self.assertEqual(stringCompression('aabb'), 'a2b2')
        self.assertEqual(stringCompression('aaabbb'), 'a3b3')


if __name__ == '__main__':
    unittest.main()
