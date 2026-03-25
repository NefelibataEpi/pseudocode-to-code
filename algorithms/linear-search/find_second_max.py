"""
Write a function:
    def find_second_max(arr):

The function should return the second largest number in the array.

Return rules:
- Return the second maximum value.
- You may assume the array has at least 2 elements.

Example:
Input:  [3, 7, 2, 9, 5]
Output: 7
"""


def find_second_max(arr):
    first = max(arr[0], arr[1])
    second = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second:
            second = arr[i]
    
    return second


def main():
    arr = [3, 7, 2, 9, 5]
    print(find_second_max(arr))


if __name__ == "__main__":
    main()