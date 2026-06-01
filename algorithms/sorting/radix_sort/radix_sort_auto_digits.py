"""
Task: Automatic Digit Count

Write a function:
    def radix_sort(arr):

Functionality:
- Automatically determine the number of digits needed, then perform radix sort.

Return rules:
- Return a NEW sorted array
- Do NOT modify the original array
- Handle empty array

Example:

Input:
[170, 45, 75, 90, 802, 24, 2, 66]

Output:
[2, 24, 45, 66, 75, 90, 170, 802]
"""

from stable_sort_by_digit import stable_sort_by_digit

def radix_sort(arr):
    if not arr:
        return arr
    
    max_num = max(arr)
    d = len(str(max_num))

    result = arr[:]

    for i in range(d):
        result = stable_sort_by_digit(result, i)

    return result


def main():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(radix_sort(arr))


if __name__ == "__main__":
    main()