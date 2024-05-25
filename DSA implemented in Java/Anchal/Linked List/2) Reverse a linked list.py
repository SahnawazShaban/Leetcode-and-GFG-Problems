"""
Reverse a linked list

Easy

Given a linked list of N nodes. The task is to reverse this list.

Example 1:
Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list, 
elements are 6->5->4->3->2->1.

Example 2:
Input:
LinkedList: 2->7->8->9->10
Output: 10 9 8 7 2
Explanation: After reversing the list,
elements are 10->9->8->7->2.

Your Task:
The task is to complete the function reverseList() with head reference as the only argument and should return new head after reversing the list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 10^4

"""

# SOLUTION

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        '''
        # TC : O(n), SC : O(1)
        cur = head
        prev = None
        while cur != None:
            temp = cur.next
            cur.next = prev

            # shifting
            prev = cur 
            cur = temp
        
        return prev

        '''


        # --------------------------
        
        ## Recursive Approach : TC - O(n), SC - O(n)
        
        # Base case: an empty list or a list with a single node is already reversed
        if head is None or head.next is None:
            return head

        reverseListHead = self.reverseList(head.next)
        
        # Adjust pointers to reverse the current node
        head.next.next = head
        head.next = None
        
        return reverseListHead
    
        # or
        '''
        if head == None or head.next == None:
            return head
            
        newHead = self.reverseList(head.next)
        headNext = head.next
        headNext.next = head
        head.next = None
        
        return newHead
        '''
    