"""
Subtraction in Linked List

Hard

You are given two linked lists that represent two large positive numbers. From the two numbers represented by the linked lists, subtract the smaller number from the larger one. Look at the examples to get a better understanding of the task.

Example 1:
Input:
L1 = 1->0->0
L2 = 1->2
Output: 88
Explanation:  
First linked list represents 100 and the
second one represents 12. 12 subtracted from 100
gives us 88 as the result. It is represented
as 8->8 in the linked list.

Example 2:
Input:
L1 = 0->0->6->3
L2 = 7->1->0
Output: 647
Explanation: 
First linked list represents 0063 => 63 and 
the second one represents 710. 63 subtracted 
from 710 gives us 647 as the result. It is
represented as 6->4->7 in the linked list.
Your Task:
You do not have to take any input or print anything. The task is to complete the function subLinkedList() that takes heads of two linked lists as input parameters and which should subtract the smaller number from the larger one represented by the given linked lists and return the head of the linked list representing the result.

n and m are the length of the two linked lists respectively.
Expected Time Complexity:  O(n+m)
Expected Auxiliary Space: O(n+m)

Constraints:
1 <= n <= 10000
0 <= values represented by the linked lists < 10^n
0 <= values represented by the linked lists < 10^m

"""

# Solution 

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def subLinkedList(self, l1, l2): 
        current1 = l1
        current2 = l2
        value1 = 0
        value2 = 0

        # Extract integer values from the first linked list
        while current1:
            value1 = value1 * 10 + current1.data
            current1 = current1.next

        # Extract integer values from the second linked list
        while current2:
            value2 = value2 * 10 + current2.data
            current2 = current2.next

        # Calculate the absolute difference
        absolute_difference = abs(value1 - value2)

        # Create a new linked list with a single node containing the absolute difference
        result_node = Node(absolute_difference)

        return result_node


'''
Time Complexity:
The algorithm iterates through both linked lists once to extract the integer values. The time complexity of this process is O(N + M), where N is the length of the first linked list (list1) and M is the length of the second linked list (list2).
The subsequent operations involving arithmetic operations and creating a new linked list have constant time complexity and do not affect the overall complexity.
Therefore, the overall time complexity is O(N + M).

Space Complexity:
The space complexity is O(1) because the algorithm uses a constant amount of extra space regardless of the input size. The space required for variables such as current1, current2, value1, value2, and result_node does not depend on the length of the linked lists.

In summary:
Time Complexity: O(N + M)
Space Complexity: O(1)
'''
    