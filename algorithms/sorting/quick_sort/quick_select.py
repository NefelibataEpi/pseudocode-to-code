"""
Implement:
    def quick_select(arr, k):

The function should return:
the k-th smallest element
using the Quick Select algorithm.

Important Rules
- Use Quick Sort partition idea
- Do NOT fully sort the array
- Average complexity should be: `O(n)`

Return Rules
- k is 0-indexed
= Return the value itself

Example
```
arr = [7, 2, 9, 1, 5]
k = 2
```
Sorted: `[1,2,5,7,9]`
Return: `5`
"""

from basic_partition import partition

def quick_select(arr, k):
    return quick_select_helper(arr, 0, len(arr), k)


def quick_select_helper(arr, start, end, k):
    if end - start == 1:
        return arr[start]
    
    pivot_index = partition(arr, start, end)

    if pivot_index == k:
        return arr[pivot_index]
    elif k < pivot_index:
        return quick_select_helper(arr, start, pivot_index, k)
    else:
        return quick_select_helper(arr, pivot_index + 1, end, k)


def main():
    arr = [7, 2, 9, 1, 5]
    k = 2
    print(quick_select(arr, k))


if __name__ == "__main__":
    main()