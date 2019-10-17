import unittest
import vending_machine.machine
import vending_machine.product
from unittest.mock import patch


class TestVendingMachine(unittest.TestCase):
    def test_product_create(self):
        p = vending_machine.product.Product()
        self.assertIsNotNone(p)

    def test_machine_create(self):
        vm = vending_machine.machine.Machine()
        self.assertIsNotNone(vm)

    def test_vm(self):
        vm = vending_machine.machine.Machine()
        with patch('builtins.input', return_value=1):
            vm.getQuantity()
        with patch('builtins.input', return_value=5):
            vm.getAmount()
        res = vm.processReq()
        self.assertEqual(res, (1, 0))

        with patch('builtins.input', return_value=1):
            vm.getQuantity()
        with patch('builtins.input', return_value=6):
            vm.getAmount()
        res = vm.processReq()
        self.assertEqual(res, (1, 1))

        with patch('builtins.input', return_value=2):
            vm.getQuantity()
        with patch('builtins.input', return_value=6):
            vm.getAmount()
        res = vm.processReq()
        self.assertEqual(res, (0, 6))

        with patch('builtins.input', return_value=-1):
            vm.getQuantity()
        with patch('builtins.input', return_value=6):
            vm.getAmount()
        res = vm.processReq()
        self.assertEqual(res, (0, 6))

        with patch('builtins.input', return_value=2):
            vm.getQuantity()
        with patch('builtins.input', return_value=16):
            vm.getAmount()
        res = vm.processReq()
        self.assertEqual(res, (2, 6))

        with patch('builtins.input', return_value=1):
            vm.getQuantity()
        with patch('builtins.input', return_value=-16):
            vm.getAmount()
        res = vm.processReq()
        self.assertEqual(res, (0, 0))

        with patch('builtins.input', return_value=4):
            vm.getQuantity()
        with patch('builtins.input', return_value=16):
            vm.getAmount()
        res = vm.processReq()
        self.assertEqual(res, (0, 16))

        with patch('builtins.input', return_value=4):
            vm.getQuantity()
        with patch('builtins.input', return_value=-1):
            vm.getAmount()
        res = vm.processReq()
        self.assertEqual(res, (0, 0))


if __name__ == '__main__':
    unittest.main()
