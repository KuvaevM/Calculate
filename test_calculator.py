import unittest
import random
import math
import time
from simple_calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        constanta = random.randint(1,1000)
        value = random.random()*constanta
        self.calculator = Calculator(2)
        print('начало теста:', time.time())

    def test_add(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)
        print('конец теста:', time.time())

    def test_mul(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)
        print('конец теста:', time.time())

    def test_divide(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(3, 3).value, calc_value / 9)
        print('конец теста:', time.time())

    def test_power(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(1).value, calc_value)
        self.assertEqual(self.calculator.power(5).value, math.pow(calc_value, 5))
        print('конец теста:', time.time())

    def test_root(self):
        calc_value = self.calculator.value
        self.assertEqual(round(self.calculator.power(100).root(100).value), calc_value)
        print('конец теста:', time.time())

    def test_difficult_function(self):
        calc_value = self.calculator.value
        self.assertEqual(pow((calc_value/2*9+5)*2/8,3), self.calculator.divide(1, 2).multiply(3, 3).add(1, 2, 2).multiply(2).divide(2, 4).power(3).value)
        print('конец теста:', time.time())

    def test_distribut(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(7).multiply(5).value, calc_value*5+5*7)
        print('конец теста:', time.time())

    def test_square(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(2, 5).power(2).value, calc_value*calc_value+2*calc_value*7+7*7)
        print('конец теста:', time.time())


if __name__ == '__main__':
    unittest.main()
