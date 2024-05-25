/*
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


Company Tags
Paytm
VMWare
Zoho
Accolite
Amazon
Microsoft
Samsung
Snapdeal
D-E-Shaw
MakeMyTrip
Teradata
Walmart
Goldman 
Sachs
Intuit
Adobe
SAP Labs
Tejas Network
Cisco
Qualcomm
Cognizant
Mahindra

Topic Tags
Linked List, Data Structures
*/

// SOLUTION

/* linked list node class:

class Node {
    int data;
    Node next;
    Node(int value) {
        this.value = value;
    }
}
*/

class Solution {
    // Function to reverse a linked list.
    Node reverseList(Node head) {
        // Solution - 1
        Node cur = head;
        Node prev = null;

        while (cur != null) {
            Node temp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = temp;
        }
        return prev;

        // Solution - 2 - Recursive Approach
        if (head == null || head.next == null) {
            return head;
        }

        Node newHead = reverseList(head.next);
        Node headNext = head.next;
        headNext.next = head;
        head.next = null;

        return newHead;
    }
}