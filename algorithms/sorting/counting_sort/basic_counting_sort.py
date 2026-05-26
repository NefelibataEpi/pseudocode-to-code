"""
##Task: Implement a basic version of Counting Sort.

### Write a function:
    `def counting_sort(arr):`

### The function should:
- Sort the array using Counting Sort
- Assume all numbers are non-negative integers
- Return a new sorted list

### Functionalities
- Find the maximum number
- Create a counting array
- Count frequencies
- Rebuild the sorted array

### Return Rules
Return the sorted array.

### Example
```
Input:
[4, 2, 2, 8, 3, 3, 1]

Output:
[1, 2, 2, 3, 3, 4, 8]
```
"""

def counting_sort(arr):
    max_num = max(arr)

    counts = [0] * (max_num + 1)
    sorted_arr = []

    for num in arr:
        counts[num] += 1
    
    for i in range(len(counts)):
        for _ in range(counts[i]):
            sorted_arr.append(i)

    return sorted_arr


def main():
    arr = [4, 2, 2, 8, 3, 3, 1]
    print(counting_sort(arr))


if __name__ == "__main__":
    main()