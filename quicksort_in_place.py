def quicksort_in_place(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quicksort_in_place(arr, low, pi - 1)
        quicksort_in_place(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1         # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot
    return i + 1

# Example usage
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    quicksort_in_place(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
