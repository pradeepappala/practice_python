import unittest
from CrackingCodingInterview.palinPerm import palinPerm
from CrackingCodingInterview.palinPerm import oneAway


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
        self.assertTrue(oneAway('pales', 'pale'))


if __name__ == '__main__':
    unittest.main()
