"""
4. Median of Two Sorted Arrays

Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6

"""

# SOLUTION

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = []
        n, m = len(nums1), len(nums2)
        i,j = 0,0

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        
        while i < n:
            temp.append(nums1[i])
            i += 1
        
        while j < m:
            temp.append(nums2[j])
            j += 1
        
        if len(temp)%2 == 1:
            ans = temp[len(temp)//2]
            return float(ans)
        else:
            ans = (temp[len(temp)//2] + temp[(len(temp)//2) - 1])/2
            return float(ans)    
        