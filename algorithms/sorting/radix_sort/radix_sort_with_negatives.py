"""
Task: Radix Sort with Negatives

Write a function:
    def radix_sort_with_negatives(arr):

Functionality:
- Sort an array containing both positive and negative integers.

Return rules:
- Return a NEW sorted array
- Do NOT modify original array
- Handle empty array

Example:

Input:
[170, -45, 75, -90, 802, 24, -2, 66]

Output:
[-90, -45, -2, 24, 66, 75, 170, 802]
"""

from stable_sort_by_digit import stable_sort_by_digit

def radix_sort_with_negatives(arr):
    if not arr:
        return arr
    
    result = []

    positive = [num for num in arr if num >= 0] 
    negative = [abs(num) for num in arr if num < 0]

    max_positive = max(positive) if positive else 0
    max_negative = max(negative) if negative else 0

    max_num = max(max_positive, max_negative)
    d = len(str(max_num))

    for i in range(d):
        positive = stable_sort_by_digit(positive, i)
        negative = stable_sort_by_digit(negative, i)
    
    negative.reverse()

    for num in negative:
        result.append(0 - num)

    for num in positive:
        result.append(num)
    
    return result


def main():
    arr = [170, -45, 75, -90, 802, 24, -2, 66]
    print(radix_sort_with_negatives(arr))


if __name__ == "__main__":
    main()