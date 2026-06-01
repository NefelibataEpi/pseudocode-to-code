"""
Write a function:
    def quick_sort(arr):

The function should sort the array in ascending order using Quick Sort.

You should also write a helper:
    def quick_sort_helper(arr, start, end):

Use the interval: `[start, end)`
So end is not included.

Functionalities
- Use Lomuto partition
- Choose the last element as pivot
- Sort the array in-place
- Return the sorted array

Return Rules
- Return arr after sorting
- If the array is empty or has one element, return it directly

Example
```
arr = [7, 2, 9, 1, 5]
print(quick_sort(arr))
```

Output: `[1, 2, 5, 7, 9]`
"""

from basic_partition import partition

def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr))
    return arr


def quick_sort_helper(arr, start, end):
    if end - start <= 1:
        return arr
    
    pivot_index = partition(arr, start, end)

    quick_sort_helper(arr, start, pivot_index)
    quick_sort_helper(arr, pivot_index + 1, end)


def main():
    arr = [7, 2, 9, 1, 5]
    print(quick_sort(arr))


if __name__ == "__main__":
    main()