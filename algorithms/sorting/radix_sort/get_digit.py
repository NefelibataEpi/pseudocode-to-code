"""
Task: Extract Digit

Write a function:
    def get_digit(num, i):

Functionality: Return the digit at position i from the right.

Return rules:
- i = 0 means ones digit
- i = 1 means tens digit
- i = 2 means hundreds digit

Example:
Input:  num = 538, i = 0
Output: 8

Input:  num = 538, i = 1
Output: 3

Input:  num = 538, i = 2
Output: 5
"""

def get_digit(num, i):
    return (num // (10 ** i)) % 10


def main():
    num = 538
    print(get_digit(num, 0))
    print(get_digit(num, 1))
    print(get_digit(num, 2))


if __name__ == "__main__":
    main()