def counting_sort(arr):
    min_num = min(arr)
    max_num = max(arr)

    counting_range = max_num - min_num + 1

    counts = [0] * counting_range
    output = [0] * len(arr)

    for num in arr:
        counts[num - min_num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1] 

    for i in range(len(arr) - 1, -1, -1):
        output[counts[arr[i] - min_num] - 1] = arr[i]
        counts[arr[i] - min_num] -= 1

    return output


def main():
    arr = [-5, -1, 3, 0]
    print(counting_sort(arr))


if __name__ == "__main__":
    main()