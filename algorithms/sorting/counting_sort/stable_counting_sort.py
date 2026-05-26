def counting_sort(arr):
    max_num = max(arr)

    counts = [0] * (max_num + 1)
    sorted_arr = [0] * len(arr)

    for num in arr:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    
    for i in range(len(arr)-1, -1, -1):
        sorted_arr[counts[arr[i]]-1] = arr[i]
        counts[arr[i]] -= 1

    return sorted_arr


def main():
    arr = [4, 2, 2, 8, 3, 3, 1]
    print(counting_sort(arr))


if __name__ == "__main__":
    main()