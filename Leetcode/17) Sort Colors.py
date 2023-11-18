"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

"""

# SOLUTION

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## Brute Force

        count = [0, 0, 0]  # Count of 0s, 1s, and 2s

        # First pass: Count occurrences of each color
        for num in nums:
            count[num] += 1

        # Second pass: Overwrite the array with the correct number of colors
        i = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[i] = color
                i += 1

        # -----------------------------------------

        ## Optimal

        n = len(nums)
        red, white, blue = 0, 0, n-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


        # Time and Space Complexity

        '''
        The provided code is an implementation of the Dutch National Flag problem, which is used to sort an array containing only three distinct elements (0, 1, and 2). Here's the analysis of its time and space complexity:

        Time Complexity:
        The code uses a single pass through the array to sort it in-place, so the time complexity is O(n), where 'n' is the length of the nums array.

        Space Complexity:
        The code uses a constant amount of extra space, regardless of the input size. It doesn't create any additional data structures that grow with the input size. Therefore, the space complexity is O(1), which means it's constant and not dependent on the size of the input array.
        '''