"""
Write a function:
    def is_sorted(arr):

The function should check whether the array is sorted in ascending order.

Return rules:
- Return True if sorted
- Return False otherwise

Example:
Input:  [1, 2, 3, 4]
Output: True

Input:  [1, 3, 2]
Output: False
"""


def is_sorted(arr):
    previous = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < previous:
            return False
        
        previous = arr[i]

    return True


def main():
    arr_1 = [1, 2, 3, 4]
    print(is_sorted(arr_1))

    arr_2 = [1, 3, 2]
    print(is_sorted(arr_2))


if __name__ == "__main__":
    main()