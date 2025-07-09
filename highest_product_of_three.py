def highest_product_of_three(nums):
    if len(nums) < 3:
        raise ValueError("Array must contain at least three numbers.")

    nums.sort()

    # Product of three largest numbers
    max1 = nums[-1] * nums[-2] * nums[-3]

    # Product of two smallest and the largest
    max2 = nums[0] * nums[1] * nums[-1]

    return max(max1, max2)

# Example usage
if __name__ == "__main__":
    arr = [-10, -10, 5, 2, 8]
    result = highest_product_of_three(arr)
    print("Highest product of three numbers:", result)
