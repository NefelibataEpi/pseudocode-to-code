"""
Task: Basic Radix Sort

Write a function:
    def radix_sort(arr, d):

Functionality:
- Sort an array of non-negative integers using radix sort.

Return rules:
- Return a NEW sorted array
- Do NOT modify the original array
- Assume every number has at most d digits

Example:

Input:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
d = 3

Output:
[2, 24, 45, 66, 75, 90, 170, 802]
"""

from stable_sort_by_digit import stable_sort_by_digit

def radix_sort(arr, d):
    for i in range(d):
        arr = stable_sort_by_digit(arr, i)

    return arr


def main():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(radix_sort(arr, 3))


if __name__ == "__main__":
    main()