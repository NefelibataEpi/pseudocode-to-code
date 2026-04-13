"""
Task: Implement Basic Insertion Sort

Write a function:
    def insertion_sort(arr):

The function should sort the input list arr in ascending order using the insertion sort algorithm.

You must follow this idea:
- Iterate from index 1 to n-1
- For each element, treat it as key
- Scan from the beginning of the array (index 0) to find the correct insertion position
- Shift elements to the right to make space
- Insert the key into the correct position

Functional Requirements:
- Modify the list in-place
- Do NOT use built-in sort functions
- Must follow the forward scanning idea (like your pseudocode)

Return the sorted array

Example:
Input:  [5, 2, 4, 6, 1, 3]
Output: [1, 2, 3, 4, 5, 6]
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = 0

        while (pos < i) and (arr[pos] < key):
            pos += 1
        
        for j in range(i-1, pos-1, -1):
            arr[j+1] = arr[j]

        arr[pos] = key
    
    return arr


def main():
    arr = [5, 2, 4, 6, 1, 3]
    print(insertion_sort(arr))


if __name__ == "__main__":
    main()