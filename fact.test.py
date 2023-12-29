# test_factorial.py

import pytest
from your_module_name import factorial  # Replace 'your_module_name' with the actual module name where your factorial function is defined

def test_factorial_positive_integer():
    assert factorial(5) == 120
    assert factorial(7) == 5040
    assert factorial(10) == 3628800

def test_factorial_zero_and_one():
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_negative_number():
    assert factorial(-5) == "Factorial is undefined for negative numbers"

def test_factorial_large_number():
    # Add more test cases as needed
    assert factorial(20) == 2432902008176640000

# Add more test cases as needed
