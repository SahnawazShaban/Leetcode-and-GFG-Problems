"""
19. Remove Nth Node From End of List

Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

# SOLUTION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Solution - 1

        '''
        dummy = ListNode(0,head)
        L = dummy
        R = head

        while R and n!=0:
            R = R.next
            n -= 1
        
        while R:
            R = R.next
            L = L.next
        
        L.next = L.next.next

        return dummy.next
        '''

        # Solution - 2
        '''
        fast = head
        slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next
            
        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head
        '''
        
        # Solution - 3

        # use dummy head will make the removal of head node easier
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        # cur keeps iteration till the end
        # prev_of_removal traverses to the previous node of the one of being removed
        cur, prev_of_removal = dummy_head, dummy_head
        
        
        while cur.next != None:
            
            # n-step delay for prev_of_removal
            if n <= 0:
                prev_of_removal = prev_of_removal.next
                
            cur = cur.next
            
            n -=1
        
        
        # Remove the N-th node from end of list
        n_th_node = prev_of_removal.next
        prev_of_removal.next = n_th_node.next
        
        del n_th_node
        
        return dummy_head.next