def binary_search(arr, target):
    return binary_search_helper(arr, target, 0, len(arr) - 1)


def binary_search_helper(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_helper(arr, target, mid + 1, right)
    else:
        return binary_search_helper(arr, target, left, mid - 1)


def main():
    arr = [1, 3, 5, 7, 9]
    print(binary_search(arr, 5)) # Output: 2
    print(binary_search(arr, 8)) # Output: -1


if __name__ == "__main__":
    main()