"""
1. Intersection of Two Arrays
Easy
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input
4 2
1 2 2 1
1 2

Output
1 2

Example 2:
Input
3 5
4 9 5
9 4 9 8 4

Output
4 9

Example 3:
Input
5 5
1 2 3 4 5
6 7 8 9 10

Output

Explaination:

In the first example, the intersection of [1,2,2,1] and [2,2] is [2,1].

In the second example, the intersection of [4,9,5] and [9,4,9,8,4] is [9,4].

In the third example, there is no intersection between [1,2,3,4,5] and [6,7,8,9,10], so the result is an empty array.

Constraints:

1 <= nums1.length, nums2.length <= 10^4
0 <= nums1[i], nums2[i] <=10^9
Input Format:

You are given two integer arrays nums1 and nums2 such that:

1 <= nums1.length, nums2.length <= 10^4
0 <= nums1[i], nums2[i] <= 10^9
Output Format:

An array of integers representing the intersection of nums1 and nums2. The result must be unique and can be returned in any order.

"""


# Solution 

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = []
        
        
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in temp:
                temp.append(nums1[i])
                
        return temp