/*
Add 1 to a number represented as linked list
Medium
A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

Example 1:
Input:
LinkedList: 4->5->6
Output: 457
Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457. 

Example 2:
Input:
LinkedList: 1->2->3
Output: 124 
Your Task:
Your task is to complete the function addOne() which takes the head of the linked list as the only argument and returns the head of the modified linked list. The driver code prints the number.
Note: The head represents the left-most digit of the number.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 10^21
*/

// SOLUTION

/*
class Node{
    int data;
    Node next;
    
    Node(int x){
        data = x;
        next = null;
    }
} 
*/

class Solution {
    public static Node addOne(Node head) {
        // edge case
        if (head == null) {
            return new Node(1);
        }

        Node newhead = reverse(head);
        int carry = 1;
        int sum = 0;
        Node node = newhead;

        while (node != null) {
            sum = node.data + carry;
            if (sum < 9) {
                node.data = sum;
                carry = 0;
            } else {
                node.data = sum % 10;
                carry = sum / 10;
            }
            if (node.next == null && carry > 0) {
                Node n = new Node(sum / 10);
                node.data = sum % 10;
                node.next = n;
                node = node.next;
            }
            node = node.next;
        }

        return reverse(newhead);
    }

    static Node reverse(Node head) {
        // edge case
        if (head == null || head.next == null) {
            return head;
        }
        Node prev = null;
        Node curr = head;
        Node next = curr.next;

        while (curr != null) {
            curr.next = prev;
            prev = curr;
            curr = next;
            if (next != null)
                next = next.next;
        }
        return prev;
    }
}
