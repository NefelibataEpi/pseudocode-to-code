"""
Write a function:
    def find_first_even(arr):

The function should return the index of the first even number in the array.

Return rules:
- Return the index of the first even number.
- If there is no even number, return -1.

Example:
Input:  [1, 3, 5, 8, 9]
Output: 3

Input:  [1, 3, 5]
Output: -1
"""


def find_first_even(arr):
    for i, value in enumerate(arr):
        if value % 2 == 0:
            return i
        
    return -1


def main():
    arr_1 = [1, 3, 5, 8, 9]
    print(find_first_even(arr_1))

    arr_2 = [1, 3, 5]
    print(find_first_even(arr_2))


if __name__ == "__main__":
    main()