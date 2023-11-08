"""
2149. Rearrange Array Elements by Sign

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.


Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
 

Constraints:

2 <= nums.length <= 2 * 105
nums.length is even
1 <= |nums[i]| <= 105
nums consists of equal number of positive and negative integers.

"""

# SOLUTION

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arrP = []
        arrN = []
        for val in nums:
            if val < 0:
                arrN.append(val)
            else:
                arrP.append(val)
        
        j, k = 0, 0
        for i in range(n):
            if i%2 == 0:
                nums[i] = arrP[j]
                j += 1
            else:
                nums[i] = arrN[k]
                k += 1

        return nums
    
        '''
        The given code rearranges the elements in the input nums list such that positive numbers appear at even indices, and negative numbers appear at odd indices. This is achieved by separating the positive and negative numbers into two separate lists (arrP and arrN) and then filling the nums list by alternately taking elements from these two lists.
The time complexity of this code is O(n), where n is the length of the nums list. The code loops through the nums list once to separate positive and negative numbers and once again to rearrange the elements, both of which are linear operations.
The space complexity is also O(n) because it uses two additional lists, arrP and arrN, to store the positive and negative numbers. The size of these lists depends on the number of positive and negative numbers in the nums list, which can be at most n.
Overall, the code has an efficient time and space complexity for rearranging the elements in the desired manner.
        '''

        # ------------------------------------

        n = len(nums)
        
        # Rearrange the elements in-place without using additional lists.
        j, k = 0, 1  # Initialize indices for positive and negative elements.
        
        while j < n and k < n:
            # Find the next positive and negative elements.
            while j < n and nums[j] >= 0:
                j += 2
            while k < n and nums[k] < 0:
                k += 2
        
            # Swap the elements if found.
            if j < n and k < n:
                nums[j], nums[k] = nums[k], nums[j]
        
        return nums

        # ------------------------------------------------

        if not nums:
            return nums
        
        newArray = [0] * len(nums)
        i, j = 0, 1
        for num in nums:
            if num > 0:
                newArray[i] = num
                i += 2
            else:
                newArray[j] = num
                j += 2
                
        return newArray
        