"""
Kth largest element in BST

Easy

Given a Binary Search Tree. Your task is to complete the function which will return the Kth largest element without doing any modification in Binary Search Tree.

Example 1:
Input:
      4
    /   \
   2     9
k = 2 
Output: 4

Example 2:
Input:
       9
        \ 
          10
K = 1
Output: 10

Your Task:
You don't need to read input or print anything. Your task is to complete the function kthLargest() which takes the root of the BST and an integer K as inputs and returns the Kth largest element in the given BST.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(H) where H is max recursion stack of height H at a given time.

Constraints:
1 <= N <= 10^5
1 <= K <= N

"""


# SOLUTION

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        arr = []
        self.inorder(root, arr)
        
        return arr[len(arr) - k]
        
    def inorder(self, root, arr):
        if root == None:
            return 
        
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)

