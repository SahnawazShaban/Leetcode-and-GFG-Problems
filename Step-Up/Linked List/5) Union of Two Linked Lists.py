"""
Union of Two Linked Lists

Medium

Given two linked lists, your task is to complete the function makeUnion(), that returns the union list of two linked lists. This union list should include all the distinct elements only and it should be sorted in ascending order.

Example 1:
Input:
L1 = 9->6->4->2->3->8
L2 = 1->2->8->6->2
Output: 
1 2 3 4 6 8 9
Explaination: 
All the distinct numbers from two lists, when sorted forms the list in the output. 

Example 2:
Input:
L1 = 1->5->1->2->2->5
L2 = 4->5->6->7->1
Output: 
1 2 4 5 6 7
Explaination: 
All the distinct numbers from two lists, when sorted forms the list in the output.
Your Task:
The task is to complete the function makeUnion() which makes the union of the given two lists and returns the head of the new list.

Expected Time Complexity: O((N+M)*Log(N+M))
Expected Auxiliary Space: O(N+M)

Constraints:
1<=N,M<=10^4

"""

# SOLUTION

class Solution:
    def union(self, head1,head2):
        # code here
        # return head of resultant linkedlist
        hset = set()
        
        n1, n2 = head1, head2
        
        while n1:
            hset.add(n1.data)
            n1 = n1.next
        
        while n2:
            hset.add(n2.data)
            n2 = n2.next
        
        hset = list(hset)
        hset.sort()
        n = len(hset)
        ll = linkedList()
        
        for i in range(n):
            ll.insert(hset[i])
        return ll.head
        