"""
Task: Implement Linear Search

Write a function:
    def linear_search(arr, target):

The function should search for the target value in the array arr,
by checking each element from left to right.

Return rules:
- If the target is found, return the index of its first occurrence.
- If the target is not found, return -1.

Example:
Input:  arr = [5, 8, 2, 9, 7], target = 2
Output: 2

Input:  arr = [5, 8, 2, 9, 7], target = 6
Output: -1
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1


def main():
    arr = [5, 8, 2, 9, 7]
    target_1 = 2
    print(linear_search(arr, target_1))

    target_2 = 6
    print(linear_search(arr, target_2))


if __name__ == "__main__":
    main()