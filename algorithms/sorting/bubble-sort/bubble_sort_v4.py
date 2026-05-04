def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    last_swap_index = n - 1
    
    for i in range(n-1):
        last_swap = i
        for j in range(last_swap_index, i, -1):
            comparisons += 1
            if (arr[j] < arr[j - 1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
                last_swap = j
        
        last_swap_index = last_swap
    
    return arr, comparisons


def main():
    arr = [1, 2, 3, 4]
    print(bubble_sort(arr))


if __name__ == "__main__":
    main()