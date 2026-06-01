"""
Write a function:
    `def first_occurrence(arr, target):`

The function should return the FIRST index where target appears.

Return Rules
- Return the first occurrence index
- Return -1 if target does not exist

Example
```
arr = [1, 2, 2, 2, 4, 5]
first_occurrence(arr, 2) # Output: 1
first_occurrence(arr, 5) # Output: 5
first_occurrence(arr, 3) # Output: -1
```
"""

def first_occurrence(arr, target):
    return first_occurrence_helper(arr, target, 0, len(arr) - 1, -1)


def first_occurrence_helper(arr, target, left, right, ans):
    if left > right:
        return ans
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        ans = mid
        return first_occurrence_helper(arr, target, left, mid - 1, ans)
    elif arr[mid] < target:
        return first_occurrence_helper(arr, target, mid + 1, right, ans)
    else:
        return first_occurrence_helper(arr, target, left, mid - 1, ans)



def main():
    arr = [1, 2, 2, 2, 4, 5]
    print(first_occurrence(arr, 2)) # Output: 1
    print(first_occurrence(arr, 5)) # Output: 5
    print(first_occurrence(arr, 3)) # Output: -1


if __name__ == "__main__":
    main()