"""
Task: Implement Optimized Bubble Sort

Write a function:
    def bubble_sort(arr):

Functionalities:
Implement bubble sort in ascending order.
This time, add a boolean flag to detect whether any swap happened during one full pass.
- If no swap happened in a pass, stop early
- Otherwise, continue sorting

Return: (arr, comparisons)

Where:
- arr is the sorted array
- comparisons is the number of times this condition is checked: if arr[j] < arr[j - 1]

Example
Input:  [1, 2, 3, 4]
Output: ([1, 2, 3, 4], 3)

Because after the first pass, no swap happens, so the algorithm stops early.

Notes
- Still sort in-place
- Do not use sorted() or .sort()
- Each pass should reset the flag
- This is your first real optimization step
"""


def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    
    for i in range(0, n-1):
        swapped = False
        for j in range(n-1, i, -1):
            comparisons += 1
            if (arr[j] < arr[j - 1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
            
        if not swapped:
            break
    
    return arr, comparisons


def main():
    arr = [1, 2, 3, 4]
    print(bubble_sort(arr))


if __name__ == "__main__":
    main()