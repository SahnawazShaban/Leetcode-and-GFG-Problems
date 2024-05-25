# Function to generate the power set of a given list of numbers
/* 
def generate_power_set(nums):
    # Get the length of the input list
    n = len(nums)
    # Initialize an empty list to store the power set
    power_set = []

    # Iterate through all possible binary representations of numbers from 0 to 2^n - 1
    for i in range(2**n):
        # Initialize an empty subset for the current binary representation
        subset = []
        
        # Check each bit in the binary representation
        for j in range(n):
            # If the j-th bit is set (1), include the corresponding element in the subset
            if (i >> j) & 1:
                subset.append(nums[j])

        # Add the current subset to the power set
        power_set.append(subset)

    # Return the final power set
    return power_set

# Example usage
nums = [1, 2, 3]
# Generate the power set for the given list
result = generate_power_set(nums)




# Function to find all subsets and calculate their sums

'''
def subsetSum(idx, nums, arr):
    # Base case: if the current index is beyond the array length
    if idx >= len(nums):
        # Add the sum of the current subset to the answer list
        ans.append(sum(arr[:]))
        return

    # Include the current element in the subset
    arr.append(nums[idx])
    # Recursively explore subsets with the current element included
    subsetSum(idx + 1, nums, arr)
    # Backtrack: Remove the current element to explore subsets without it
    arr.pop()
    # Recursively explore subsets without the current element
    subsetSum(idx + 1, nums, arr)

# Input array
nums = [1, 2, 3]
# List to store the sums of all subsets
ans = []
# Start the recursion with the initial index 0 and an empty subset
subsetSum(0, nums, [])


# Output:

# Input array: [1, 2, 3]
# Sums of all subsets: [6, 3, 5, 2, 4, 1, 3, 0]
'''
*/