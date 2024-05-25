"""
108. Convert Sorted Array to Binary Search Tree

Easy

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.

"""


# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution - 1
    '''
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
    '''

    # Solution - 2
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBST(nums, start, end):
            if start <= end:
                mid = (start+end) // 2
                root = TreeNode(nums[mid])

                root.left = makeBST(nums, start, mid-1)
                root.right = makeBST(nums, mid+1, end)

                return root

        return makeBST(nums, 0, len(nums)-1)

    '''
    Time Complexity:
    The time complexity of the code is O(n), where n is the number of elements in the input array. This is because each element in the array is visited exactly once during the construction of the binary search tree.

    Space Complexity:
    The space complexity is O(log n) due to the maximum depth of the recursive call stack. In a balanced binary search tree, the depth of the recursion is log(n). Each recursive call consumes a constant amount of space, and the maximum space is determined by the depth of the recursion.

    Note: The space complexity can be O(n) in the worst case if the binary search tree is highly unbalanced (essentially becoming a linked list), but this is uncommon when dealing with sorted arrays.
    '''
