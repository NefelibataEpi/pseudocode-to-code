"""
implement a function:
    def partition(arr, pivot_index):

The function should:
- Use the element at pivot_index as the pivot
- Move all elements smaller than the pivot to the left
- Move all elements greater than or equal to the pivot to the right
- Return the final index of the pivot

You may modify the original array.

Important Rules
You should use: Lomuto Partition Scheme

Meaning:
- Move pivot to the end first
- Use:
    - i → boundary of smaller elements
    - j → scanning pointer
- Finally move pivot back to its correct position

Return: final pivot index

Example
Example 1

Input:
```
arr = [7, 2, 9, 1, 5]
pivot_index = 4
```
Possible result:
```
arr = [2, 1, 5, 7, 9]
return 2
```
Example 2

Input:
```
arr = [4, 8, 3, 2, 7]
pivot_index = 0
```
Possible result:
```
arr = [3, 2, 4, 8, 7]
return 2
```
"""

def partition(arr, start, end):
    pivot = arr[end - 1]
    i = start

    for j in range(start, end - 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[end - 1] = arr[end - 1], arr[i]

    return i