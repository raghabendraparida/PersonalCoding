def odd_even_sort(arr):
    n = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        # Perform odd indexed passes
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        # Perform even indexed passes
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

# Example usage
if __name__ == "__main__":
    arr = [34, 2, 10, -9, 7, 3, 1]
    print("Original array:", arr)
    odd_even_sort(arr)
    print("Sorted array:", arr)
