"""
Task: Count Digit Frequency

Write a function:
    def count_digit_frequency(arr, i):

Functionality:
- Count how many times each digit (0-9) appears at digit position i.

Return rules:
- Return a count array of size 10
- `count[d]` represents how many numbers contain digit d at position i

Example:

Input:
arr = [170, 45, 75, 90]
i = 0

Digits:
170 -> 0
45  -> 5
75  -> 5
90  -> 0

Output:
[2,0,0,0,0,2,0,0,0,0]
"""

from get_digit import get_digit

def count_digit_frequency(arr, i):
    count = [0] * 10

    for num in arr:
        digit = get_digit(num, i)
        count[digit] += 1
    
    return count


def main():
    arr = [170, 45, 75, 90]
    print(count_digit_frequency(arr, 0))


if __name__ == "__main__":
    main()