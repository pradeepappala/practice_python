import unittest
import calc
from unittest import mock
from unittest.mock import patch, PropertyMock


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1,0), 1)
        self.assertEqual(calc.add(1,1), 2)
        self.assertEqual(calc.add(1,-1), 0)
        self.assertEqual(calc.add(-1,-1), -2)

    def test_sub(self):
        self.assertEqual(calc.sub(1, 0), 1)
        self.assertEqual(calc.sub(1, 1), 0)
        self.assertEqual(calc.sub(1, -1), 2)
        self.assertEqual(calc.sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(calc.mul(1, 0), 0)
        self.assertEqual(calc.mul(1, 1), 1)
        self.assertEqual(calc.mul(1, -1), -1)
        self.assertEqual(calc.mul(-1, -1), 1)

    def test_pow(self):
        self.assertEqual(calc.pow(2, 0), 1)
        self.assertEqual(calc.pow(2, 1), 2)
        self.assertEqual(calc.pow(2, -1), 0.5)
        self.assertEqual(calc.pow(-2, -1), -0.5)

    def test_mock(self):
        with mock.patch('calc.MyClass.last_transaction', new_callable=PropertyMock) as mock_last_transaction:
            mock_last_transaction.return_value = True
            myclass = calc.MyClass()
            print(myclass.last_transaction)
            mock_last_transaction.assert_called_once_with()

    @patch('calc.MyClass.last_transaction', new_callable=PropertyMock)
    def test_1(mock_last_transaction):
        mock_last_transaction.return_value = True
        myclass = calc.MyClass()
        print(myclass.last_transaction)
        mock_last_transaction.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
