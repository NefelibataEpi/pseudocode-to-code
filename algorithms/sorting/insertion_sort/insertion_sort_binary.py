
def main():
    arr = [5, 2, 4, 6, 1, 3]
    print(insertion_sort_binary(arr))


def insertion_sort_binary(arr):
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            continue

        key = arr[i]
        pos = binary_search(arr, key, 0, i-1)
        for j in range(i-1, pos-1, -1):
            arr[j+1] = arr[j]
        arr[pos] = key

    return arr


def binary_search(arr, key, left, right):
    if left > right:
        return left
    
    mid = (left + right) // 2

    if (arr[mid] >= key):
        return binary_search(arr, key, left, mid-1)
    else:
        return binary_search(arr, key, mid+1, right)


if __name__ == "__main__":
    main()