"""
Write a function:
    def bubble_sort(arr):

Requirements:

- Sort the array in ascending order
- Modify the array in-place
- Follow the pseudocode logic exactly

Do NOT use:
    sorted()
    .sort()

Example:
Input:  [5, 3, 8, 2]
Output: [2, 3, 5, 8]
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(n-1, i, -1):
            if (arr[j] < arr[j - 1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
    
    return arr


def main():
    arr = [5, 3, 8, 2]
    print(bubble_sort(arr))


if __name__ == "__main__":
    main()