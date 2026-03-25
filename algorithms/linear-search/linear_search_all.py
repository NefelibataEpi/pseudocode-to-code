"""
Write a function:
    def linear_search_all(arr, target):

The function should search for all occurrences of target in the array.

Return rules:
- Return a list of all indices where the target appears.
- If the target does not exist, return an empty list [].

Example:
Input:  arr = [1, 3, 5, 3, 7, 3], target = 3
Output: [1, 3, 5]

Input:  arr = [1, 2, 4], target = 6
Output: []
"""

def linear_search_all(arr, target):
    result = []

    for i, value in enumerate(arr):
        if value == target:
            result.append(i)

    return result


def main():
    arr_1 = [1, 3, 5, 3, 7, 3]
    target_1 = 3
    print(linear_search_all(arr_1, target_1))

    arr_2 = [1, 2, 4]
    target_2 = 6
    print(linear_search_all(arr_2, target_2))


if __name__ == "__main__":
    main()