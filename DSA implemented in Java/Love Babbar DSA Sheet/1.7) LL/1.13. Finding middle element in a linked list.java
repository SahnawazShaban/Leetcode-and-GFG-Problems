/*
Finding middle element in a linked list
EasyAccuracy: 57.93%Submissions: 306K+Points: 2
Matrix Partners India: Exclusive Job-A-Thon | Apply to 15+ Companies via 1 Hiring Challenge | Starting from 29th April onwards

banner
Given a singly linked list of N nodes.
The task is to find the middle of the linked list. For example, if the linked list is
1-> 2->3->4->5, then the middle node of the list is 3.
If there are two middle nodes(in case, when N is even), print the second middle element.
For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.

Example 1:
Input:
LinkedList: 1->2->3->4->5
Output: 3 
Explanation: 
Middle of linked list is 3.
Example 2: 
Input:
LinkedList: 2->4->6->7->5->1
Output: 7 
Explanation: 
Middle of linked list is 7.
Your Task:
The task is to complete the function getMiddle() which takes a head reference as the only argument and should return the data at the middle node of the linked list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 5000
*/


// SOLUTION

/* Node of a linked list
 class Node {
   int data;
    Node next;
    Node(int d)  { data = d;  next = null; }
}
*/

class Solution {
    // Solution - 1
    int getMiddle(Node head) {
        // if (head == null) return head;

        Node slow = head;
        Node fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow.data;
    }

    // Solution - 2
    static int getLen(Node head) {
        int len = 0;
        Node temp = head;
        // Traverse the entire linked list and increment len
        // by 1 for each node
        while (temp != null) {
            len++;
            temp = temp.next;
        }
        // Return the number of nodes in the linked list
        return len;
    }

    // Function to get the middle value of the linked list
    static int getMiddle(Node head) {
        // find length
        int len = getLen(head);
        Node temp = head;

        // traverse till we reached half of length
        int midIdx = len / 2;
        while (midIdx > 0) {
            temp = temp.next;
            midIdx--;
        }
        // temp will be storing middle element
        return temp.data;
    }

}
