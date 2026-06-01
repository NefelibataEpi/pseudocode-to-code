"""
Task: Stable Sort By Digit

Write a function:
    def stable_sort_by_digit(arr, i):

Functionality:
- Sort the array according to digit position i, while preserving relative order of equal digits.

Return rules:
- Return a NEW sorted array
- Do NOT modify the original array
- The sorting must be stable

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
[170, 90, 45, 75]
"""

from get_digit import get_digit
from count_digit_frequency import count_digit_frequency

def stable_sort_by_digit(arr, i):
    counts = count_digit_frequency(arr, i)
    sorted_arr = [0] * len(arr)

    for j in range(1, len(counts)):
        counts[j] += counts[j-1]

    for k in range(len(arr)-1, -1, -1):
        digit = get_digit(arr[k], i)
        sorted_arr[counts[digit] - 1] = arr[k]
        counts[digit] -= 1
    
    return sorted_arr


def main():
    arr = [170, 45, 75, 90]
    print(stable_sort_by_digit(arr, 0))


if __name__ == "__main__":
    main()