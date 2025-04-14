#https://github.com/Domedigger/lab10-JT-MG.git
#Partner 1: Jordon Taylor
#Partner 2: Morgan Granade

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
    # def test_subtract(self): # 3 assertions
    #     fill in code
    def test_sub(self):
        self.assertEqual(subtract(5, 3), 2)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code
    def test_multiply(self):
        self.assertEqual(mul(3,4), 12)
        self.assertEqual(mul(-2,5), -10)
        self.assertEqual(mul(0,10), 0)

    # def test_divide(self): # 3 assertions
    #     fill in code
    def test_divide(self):
        self.assertEqual(div(2,6), 3)
        self.assertEqual(div(1,5), 5)
        self.assertEqual(div(1,1), 1)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,5)
    # def test_logarithm(self): # 3 assertions
    #     fill in code
    def test_logarithm(self):
        self.assertEqual(logarithm(5, 25), 2)
    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)
            logarithm(1,3)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6,8), 10)
        self.assertEqual(hypotenuse(-3, 4), 5)

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(5), 2.236, 3)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()