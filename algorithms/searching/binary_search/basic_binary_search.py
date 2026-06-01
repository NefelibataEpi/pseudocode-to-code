"""
Task: Implement Binary Search using iteration.

Write a function:
    def binary_search(arr, target):

The function should search for target
inside a sorted array arr.

Functionalities
- Use binary search logic
- Use two pointers: `left`, `right`
- Repeatedly check the middle element

Return Rules
- Return the index if target is found
- Return -1 if target does not exist

Example

```
arr = [1, 3, 5, 7, 9]
binary_search(arr, 7) # Output: 3
binary_search(arr, 2) # Output: -1
```
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    arr = [1, 3, 5, 7, 9]
    print(binary_search(arr, 7)) # Output: 3
    print(binary_search(arr, 2)) # Output: -1


if __name__ == "__main__":
    main()