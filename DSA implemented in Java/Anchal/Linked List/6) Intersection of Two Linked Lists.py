"""
160. Intersection of Two Linked Lists

Easy

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

 

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 10^4
1 <= Node.val <= 10^5
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
 

"""

# SOLUTION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Gives us TLE
    # Faster than 81.92% (At that time ;)
    def usingSets(self, headA, headB):
        visited = set()
        while headA:
            visited.add(headA)
            headA = headA.next
        
        while headB:
            if headB in visited: return headB
            headB = headB.next
        return None
    def bruteForce(self, headA, headB):
        while headA:
            temp = headB
            while temp:
                if temp == headA: return headA
                temp = temp.next
            headA = headA.next
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB

        while temp1 != temp2:
            if temp1 == None:
                temp1 = headB
            else:
                temp1 = temp1.next

            if temp2 != None:
                temp2 = headA
            else:
                temp2 = temp2.next
            
        return temp1

        # -------------------------------------

        one = headA
        two = headB

        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one

        # ---------------------------------

        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            l1, l2 = headA, headB# First we are taking two pointers
            while l1!=l2:  # if heads are equal this implies that we found our intersection node and then we`ll return it.
                if l1: # if list1 is there then go ahead.
                    l1=l1.next # we traverse to the list to check if we found the intersection node.
                else:
                    l1 = headB # if we reach to the end of the list1 then we will move our pointer to the other list head, WHY: - explained separately below.
                # above if condition in comprehension approach. 
                # l1=l1.next if l1 else headB 
                if l2:  # if list2 is there then go ahead.
                    l2=l2.next # we traverse to the list to check if we found the intersection node.
                else:
                    l2 = headA # if we reach to the end of the list2 then we will move our pointer to the other list head, WHY: - explained separately below.
                # above if condition in comprehension approach. 
                # l2=l2.next if l2 else headA
            return l1 # returning the pointer, we could return l2 also as we found our intersection else null.

        # -----------------------------------

        first_set=set()
        curr=headA
        
        while curr:
            first_set.add(curr)
            curr=curr.next
        
        curr = headB
        while curr:
            if curr in first_set:
                return curr
            curr=curr.next

        return None
        