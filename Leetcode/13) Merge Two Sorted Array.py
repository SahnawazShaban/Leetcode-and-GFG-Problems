"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].


Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?

"""

# SOLUTION

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        p_merge = m+n-1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p_merge] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_merge] = nums2[p2]
                p2 -= 1
            p_merge -= 1

        while p2 >= 0:
            nums1[p_merge] = nums2[p2]
            p2 -= 1
            p_merge -= 1


        # --------------------------
        '''
        Intuition : 

        We are given two sorted arrays nums1 and nums2 of sizes m and n, respectively. We need to merge these two arrays into a single sorted array, and the result should be stored inside nums1. Since nums1 is of size m+n, we can use this extra space to store the merged array. We can iterate through the arrays from the end and place the larger element in the end of nums1.

        Approach : 

        Traverse through nums2 and append its elements to the end of nums1 starting from index m.
        Sort the entire nums1 array using sort() function.
        Complexity
        Time complexity: O((m+n)log(m+n))
        due to the sort() function

        Space complexity: O(1)
        We are not using any extra space, so the space complexity is O(1).

        Code
        class Solution(object):
            def merge(self, nums1, m, nums2, n):
                for j in range(n):
                    nums1[m+j] = nums2[j]
                nums1.sort()

        Approach : Two Pointer

        We can start with two pointers i and j, initialized to m-1 and n-1, respectively. We will also have another pointer k initialized to m+n-1, which will be used to keep track of the position in nums1 where we will be placing the larger element. Then we can start iterating from the end of the arrays i and j, and compare the elements at these positions. We will place the larger element in nums1 at position k, and decrement the corresponding pointer i or j accordingly. We will continue doing this until we have iterated through all the elements in nums2. If there are still elements left in nums1, we don't need to do anything because they are already in their correct place.

        Complexity
        Time complexity: O(m+n)
        We are iterating through both arrays once, so the time complexity is O(m+n).

        Space complexity: O(1)
        We are not using any extra space, so the space complexity is O(1).

        Code
        class Solution(object):
            def merge(self, nums1, m, nums2, n):
                i = m - 1
                j = n - 1
                k = m + n - 1
                
                while j >= 0:
                    if i >= 0 and nums1[i] > nums2[j]:
                        nums1[k] = nums1[i]
                        i -= 1
                    else:
                        nums1[k] = nums2[j]
                        j -= 1
                    k -= 1

        '''
        
    