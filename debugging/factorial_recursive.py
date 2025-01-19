#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function calculates the factorial of a given number using recursion.

    Parameters:
    n (int): The number for which the factorial is calculated. The function 
             works by recursively multiplying n with the factorial of n-1.

    Returns:
    int: The factorial of the number n. If n is 0, it returns 1 as the base case.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the command line argument and calculate the factorial
f = factorial(int(sys.argv[1]))
print(f)