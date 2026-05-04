"""
Write a function:
    def fast_power(base, exponent):

The function should compute:
    base**exponent
using the fast exponentiation (binary exponentiation) method (NOT using **).

Requirements
- Use an iterative approach
- Time complexity should be O(log n)
- Do NOT use recursion
- Do NOT use built-in power functions

Example:
Input:  base = 2, exponent = 10
Output: 1024

Input:  base = 3, exponent = 5
Output: 243
"""

import math


def main():
    print(fast_power(3, 5))


def fast_power(base, exponent):
    if (exponent < 0):
        exponent = -exponent
        base = 1 / base
    
    result = 1

    while (exponent > 0):
        if (exponent % 2 == 1):
            result *= base
        base *= base
        exponent //= 2
    
    return result

if __name__ == "__main__":
    main()