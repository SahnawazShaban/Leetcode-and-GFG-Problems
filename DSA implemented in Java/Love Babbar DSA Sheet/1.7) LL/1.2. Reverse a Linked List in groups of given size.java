/*
Reverse a Linked List in groups of given size
Medium
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).

Example 1:
Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5 
Explanation: 
The first 4 elements 1,2,2,4 are reversed first 
and then the next 4 elements 5,6,7,8. Hence, the 
resultant linked list is 4->2->2->1->8->7->6->5.

Example 2:
Input:
LinkedList: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4 
Explanation: 
The first 3 elements are 1,2,3 are reversed 
first and then elements 4,5 are reversed.Hence, 
the resultant linked list is 3->2->1->5->4.
Your Task:
You don't need to read input or print anything. Your task is to complete the function reverse() which should reverse the linked list in group of size k and return the head of the modified linked list.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)

Constraints:
1 <= N <= 10^5
1 <= k <= N
*/

// SOLUTION

class Solution {
    public static Node reverse(Node node, int k) {
        // Solution - 1
        if (node == null || node.next == null || k <= 1) {
            return node;
        }
        Node cur = node;
        Node temp = cur.next;
        Node prev = null;

        while (cur != null) {
            Node last = prev;
            Node nend = cur;

            for (int i = 0; cur != null && i < k; i++) {
                cur.next = prev;
                prev = cur;
                cur = temp;
                if (temp != null) {
                    temp = temp.next;
                }
            }
            if (last != null) {
                last.next = prev;
            } else {
                node = prev;
            }

            nend.next = cur;
            prev = nend;
        }

        return node;

        // Solution - 2
        if (node == null) {
            return null;
        }
        Node cur = node;
        Node temp = null;
        Node prev = null;
        int count = 0;

        while (count < k && cur != null) {
            temp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = temp;
            count++;
        }

        // Recursively reverse the next group of k nodes
        if (temp != null) {
            node.next = reverse(temp, k);
        }

        // prev now points to the head of the reversed list
        return prev;
    }
}
