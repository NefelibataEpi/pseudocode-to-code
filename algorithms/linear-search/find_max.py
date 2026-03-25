"""
Write a function:
    def find_max(arr):

The function should return the maximum value in the array.

Return rules:
- Return the maximum value.
- You may assume the array is not empty.

Example:
Input:  [3, 7, 2, 9, 5]
Output: 9
"""


def find_max(arr):
    current_max = arr[0]

    for value in arr:
        if value > current_max:
            current_max = value
    
    return current_max


def main():
    arr = [3, 7, 2, 9, 5]
    print(find_max(arr))


if __name__ == "__main__":
    main()