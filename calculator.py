"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def logarithm(a, b):
    if b <= 0 or a <= 0 or a == 1:
        raise ValueError
    return math.log(b, a)

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exponent(a, b): return a ** b

