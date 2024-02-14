"""
  Introduction To Linked List

Easy

You are given an array ‘Arr’ of size ‘N’ consisting of positive integers.

Make a linked list from the array and return the head of the linked list.

The head of the linked list is the first element of the array, and the tail of the linked list is the last element.

Note:
In the output, you will see the elements of the linked list made by you.

Example:
Input: ‘Arr’ = [4, 2, 5, 1]
Output: 4 2 5 1

Explanation: Linked List for the array ‘Arr’ = [4, 2, 5, 1] is 4 -> 2 -> 5 -> 1.
Detailed explanation ( Input/output format, Notes, Images )

Sample Input 1:
4
4 2 5 1
Sample Output 1 :
4 2 5 1

Explanation Of Sample Input 1:
Linked List for the array ‘Arr’ = [4, 2, 5, 1] is 4 -> 2 -> 5 -> 1.

Sample Input 2:
5
4 3 2 1 5

Sample Output 2:
4 3 2 1 5

Explanation Of Sample Input 2:
Linked List for the array ‘Arr’ = [4, 3, 2, 1, 5] is 4 -> 3 -> 2 -> 1 -> 5.

Expected time complexity:
The expected time complexity is O(N).


Constraints:
1 <= ‘N’ <= 10^4
1 <= ‘Arr[i]’ <= 10^5

Time Limit: 1 second

"""


# Solution 

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Do not change code above.


def constructLL(arr: [int]) -> Node:
    if not arr:
        return None

    head = Node(arr[0])
    cur = head

    for i in range(1, len(arr)):
        head.next = Node(arr[i])
        head = head.next

    head.next = None

    return cur