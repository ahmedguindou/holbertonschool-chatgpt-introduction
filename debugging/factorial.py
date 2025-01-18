#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  
    return result

if len(sys.argv) != 2:
    print("Usage: python3 script.py <non-negative-integer>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        print("Error: Please provide a non-negative integer.")
        sys.exit(1)
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)

f = factorial(num)
print(f)
