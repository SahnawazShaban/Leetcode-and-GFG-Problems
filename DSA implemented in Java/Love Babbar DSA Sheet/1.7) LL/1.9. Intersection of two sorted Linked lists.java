/*
Intersection of two sorted Linked lists
Easy
Given two linked lists sorted in increasing order, create a new linked list representing the intersection of the two linked lists. The new linked list should be made with without changing the original lists.

Note: The elements of the linked list are not necessarily distinct.

Example 1:
Input:
LinkedList1 = 1->2->3->4->6
LinkedList2 = 2->4->6->8
Output: 2 4 6
Explanation: For the given two
linked list, 2, 4 and 6 are the elements
in the intersection.

Example 2:
Input:
LinkedList1 = 10->20->40->50
LinkedList2 = 15->40
Output: 40


Your Task:
You don't have to take any input of print anything. Your task is to complete the function findIntersection(), which will take head of both of the linked lists as input and should find the intersection of two linked list and add all the elements in intersection to the third linked list and return the head of the third linked list.

Expected Time Complexity : O(n+m)
Expected Auxilliary Space : O(n+m)
Note: n, m are the size of the respective linked lists.

Constraints:
1 <= size of linked lists <= 5000
1 <= Data in linked list nodes <= 10^4
*/

// SOLUTION

class Solution {
    public static Node findIntersection(Node head1, Node head2) {
        Node a = head1;
        Node b = head2;

        Node dummy = new Node(0);
        Node ans = dummy;

        while (a != null && b != null) {
            if (a.data < b.data) {
                a = a.next;
            } else if (a.data > b.data) {
                b = b.next;
            } else {
                ans.next = new Node(a.data); // if you simply write ans.next = a, then it connect whole remaining
                                             // element of 'a' Node.
                ans = ans.next;
                a = a.next;
                b = b.next;
            }
        }
        return dummy.next;
    }
}

// Recursive Approach
public class GFG {

    // Link list node
    static class Node {
        int data;
        Node next;
    };

    static Node sortedIntersect(Node a, Node b) {

        // base case
        if (a == null || b == null)
            return null;

        /* If both lists are non-empty */

        /*
         * Advance the smaller list and
         * call recursively
         */
        if (a.data < b.data)
            return sortedIntersect(a.next, b);

        if (a.data > b.data)
            return sortedIntersect(a, b.next);

        // Below lines are executed only
        // when a.data == b.data
        Node temp = new Node();
        temp.data = a.data;

        // Advance both lists and call recursively
        temp.next = sortedIntersect(a.next, b.next);
        
        return temp;
    }

    /* UTILITY FUNCTIONS */
    /*
     * Function to insert a node at
     * the beginning of the linked list
     */
    static Node push(Node head_ref, int new_data) {

        /* Allocate node */
        Node new_node = new Node();

        /* Put in the data */
        new_node.data = new_data;

        /* Link the old list of the new node */
        new_node.next = head_ref;

        /* Move the head to point to the new node */
        head_ref = new_node;
        return head_ref;
    }

    /*
     * Function to print nodes in
     * a given linked list
     */
    static void printList(Node node) {
        while (node != null) {
            System.out.print(" " + node.data);
            node = node.next;
        }
    }

    // Driver code
    public static void main(String[] args) {

        /* Start with the empty lists */
        Node a = null;
        Node b = null;
        Node intersect = null;

        /*
         * Let us create the first sorted
         * linked list to test the functions
         * Created linked list will be
         * 1.2.3.4.5.6
         */
        a = push(a, 6);
        a = push(a, 5);
        a = push(a, 4);
        a = push(a, 3);
        a = push(a, 2);
        a = push(a, 1);

        /*
         * Let us create the second sorted linked list
         * Created linked list will be 2.4.6.8
         */
        b = push(b, 8);
        b = push(b, 6);
        b = push(b, 4);
        b = push(b, 2);

        /* Find the intersection two linked lists */
        intersect = sortedIntersect(a, b);

        System.out.print("\n Linked list containing "
                + "common items of a & b \n ");
        printList(intersect);

    }
}
