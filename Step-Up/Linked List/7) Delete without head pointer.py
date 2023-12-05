"""
Delete without head pointer

Easy

You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. The task is to delete the node. Pointer/ reference to head node is not given. 
Note: No head reference is given to you. It is guaranteed that the node to be deleted is not a tail node in the linked list.

Example 1:
Input:
N = 2
value[] = {1,2}
node = 1
Output: 2
Explanation: After deleting 1 from the
linked list, we have remaining nodes
as 2.

Example 2:
Input:
N = 4
value[] = {10,20,4,30}
node = 20
Output: 10 4 30
Explanation: After deleting 20 from
the linked list, we have remaining
nodes as 10, 4 and 30.

Your Task:
You only need to complete the function deleteNode that takes reference to the node that needs to be deleted. The printing is done automatically by the driver code.

Expected Time Complexity : O(1)
Expected Auxilliary Space : O(1)

Constraints:
2 <= N <= 10^3

"""

# SOLUTION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        # Solution - 1
        '''
        curr_node.data = curr_node.next.data
        curr_node.next = curr_node.next.next
        '''
        
        # Solution - 2
        prev = curr_node
        cur = curr_node.next
        next_node = curr_node.next.next
        
        prev.data = cur.data
        prev.next = next_node
        del cur 
        
        return 
        