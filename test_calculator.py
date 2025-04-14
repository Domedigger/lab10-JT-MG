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
        self.assertEqual(sub(5, 3), 2)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
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
            logarithm(5,0)
            logarithm(1,3)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()