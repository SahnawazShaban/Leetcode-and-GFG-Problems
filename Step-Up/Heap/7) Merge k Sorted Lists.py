"""
23. Merge k Sorted Lists

Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.

"""

# SOLUTION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize an empty heap to store tuples of the form (node.val, index, node)
        result = []
        
        # Initialize a dummy node and a tail pointer for the merged linked list
        head = tail = ListNode(0)
        
        # Initialize the index variable
        i = 0
        
        # Loop through each linked list in the input
        for i in range(len(lists)):
            # Check if the current linked list is not None
            if lists[i]:
                # Push the first node of each linked list into the heap
                heapq.heappush(result, (lists[i].val, i, lists[i]))

        # Main loop for merging
        while result:
            # Pop the node with the minimum value from the heap
            node = heapq.heappop(result)
            # Extract the actual node from the tuple
            node = node[2]

            # Connect the node to the merged linked list
            tail.next = node
            tail = tail.next

            # If the node has a next element, push it back into the heap
            if node.next:
                i += 1
                heapq.heappush(result, (node.next.val, i, node.next))

        # Return the merged linked list starting from the next of the dummy node
        return head.next
    

'''
Time Complexity:

Initialization of the Heap:
The loop that initializes the heap iterates through each linked list once, and each node is pushed onto the heap. In the worst case, this is done for all nodes in all linked lists.
The time complexity for this part is O(N log K), where N is the total number of nodes and K is the number of linked lists.

Main Loop:
In each iteration of the main loop, a node is popped from the heap, and its next node is pushed onto the heap if it exists.
Each node is pushed and popped from the heap once, and there are at most N nodes in total.
The time complexity for this part is O(N log K).
Overall, the time complexity is dominated by the heap operations, resulting in a final time complexity of O(N log K).


Space Complexity:

Heap:
The space required for the heap is O(K) since, at any given time, there are at most K nodes in the heap.

Result Linked List:
The space required for the result linked list is O(N) since, in the worst case, all nodes need to be stored in the result list.

Other Variables:
The space required for other variables (like the dummy node, tail pointer, and index variable) is constant.
Overall, the space complexity is O(N + K).
'''
