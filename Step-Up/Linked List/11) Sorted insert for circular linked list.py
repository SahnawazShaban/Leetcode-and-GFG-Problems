"""
Sorted insert for circular linked list

Easy

Given a sorted circular linked list of length n, the task is to insert a new node in this circular list so that it remains a sorted circular linked list.

Example 1:
Input:
n = 3
LinkedList = 1->2->4
(the first and last node is connected, i.e. 4 --> 1)
data = 2
Output: 
1 2 2 4
Explanation:
We can add 2 after the second node.

Example 2:
Input:
n = 4
LinkedList = 1->4->7->9
(the first and last node is connected, i.e. 9 --> 1)
data = 5
Output: 
1 4 5 7 9
Explanation:
We can add 5 after the second node.

Your Task:
The task is to complete the function sortedInsert() which should insert the new node into the given circular linked list and return the head of the linked list.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
0 <= n <= 10^5

"""

# SOLUTION

'''
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  '''
class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # Case: Empty linked list
        if not head:
            new_node.next = new_node
            return new_node

        current = head

        # Case: Insert at the beginning
        if data < head.data:
            while current.next != head:
                current = current.next
            current.next = new_node
            new_node.next = head
            return new_node

        # Case: Insert in the middle or at the end
        while current.next != head and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return head
    