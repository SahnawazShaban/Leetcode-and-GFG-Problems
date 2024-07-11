/*
Reverse a Doubly Linked List
Easy
Given a doubly linked list of n elements. Your task is to reverse the doubly linked list in-place.

Example 1:
Input:
LinkedList: 3 <--> 4 <--> 5
Output: 5 4 3

Example 2:
Input:
LinkedList: 75 <--> 122 <--> 59 <--> 196
Output: 196 59 122 75
Your Task:
Your task is to complete the given function reverseDLL(), which takes head reference as argument and this function should reverse the elements such that the tail becomes the new head and all pointers are pointing in the right order. You need to return the new head of the reversed list. The printing and verification is done by the driver code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 <= number of nodes <= 10^4
0 <= value of nodes <= 10^4

Company Tags
D-E-Shaw, Adobe
*/

// SOLUTION

class Node
{
    int data;
    Node next, prev;
    Node(int data)
    {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

public static Node reverseDLL(Node  head)
{
    Node cur = head;
    while (cur != null){
        Node temp = cur.next;
        cur.next = cur.prev;
        cur.prev = temp;
        
        head = cur;
        cur = cur.prev;
    }
    return head;
}