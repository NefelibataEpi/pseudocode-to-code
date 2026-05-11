"""
## Task: Count Smaller Elements After Self

Write a function:

```python
def count_smaller(nums):
```

---

Functionalities:

For each element, count how many elements to its right are smaller.

---

Return rules:

- Return a list
- Same length as nums

---

Example:

```
Input:  [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```
"""

def count_smaller(nums):
    result = [0] * len(nums)
    arr = [(nums[i], i) for i in range(len(nums))]

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)
    
    def merge(left, right):
        merged = []
        i = j = 0
        count = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                result[left[i][1]] += count
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                count += 1
                j += 1
            
        while i < len(left):
            result[left[i][1]] += count
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged
    
    merge_sort(arr)
    return result


# Test
nums = [5, 2, 6, 1]
print(count_smaller(nums))

arr = [2, 4, 1, 3, 5]
print(count_smaller(arr))