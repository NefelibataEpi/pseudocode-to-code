import insertion_sort_basic
import insertion_sort_backward
import insertion_sort_binary


def main():
    arr = [5, 2, 4, 6, 1, 3]
    print(sort_array(arr, method="basic"))


def sort_array(arr, method):
    match method:
        case "basic": return insertion_sort_basic.insertion_sort(arr)
        case "backward": return insertion_sort_backward.insertion_sort(arr)
        case "binary": return insertion_sort_binary.insertion_sort_binary(arr)
        case _:
            raise ValueError(f"Unknown method: {method}")


if __name__ == "__main__":
    main()