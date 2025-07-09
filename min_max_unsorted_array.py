# Function to find the smallest and largest elements in an unsorted array
def find_smallest_largest(arr):
    if not arr:
        return None, None  # Handle empty array

    smallest = largest = arr[0]

    for num in arr[1:]:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest

# Example usage
if __name__ == "__main__":
    arr = [3, 5, 1, 2, 4, 8, 0, -1]
    smallest, largest = find_smallest_largest(arr)
    print("Smallest element:", smallest)
    print("Largest element:", largest)
