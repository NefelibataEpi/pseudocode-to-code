"""
Write a function:
    def selection_sort(arr):

The function should sort the array in ascending order using the Selection Sort algorithm.

Input: A list of integers arr
Output: Return the sorted list

Example:
Input:  [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]
"""


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def main():
    arr = [64, 25, 12, 22, 11]
    print(selection_sort(arr))


if __name__ == "__main__":
    main()