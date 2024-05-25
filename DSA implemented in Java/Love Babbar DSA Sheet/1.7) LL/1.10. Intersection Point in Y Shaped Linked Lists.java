/*
Intersection Point in Y Shaped Linked Lists
Medium
Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.

Example 1:
Input:
LinkList1 = 3->6->9->common
LinkList2 = 10->common
common = 15->30->NULL
Output: 15
Explanation:
Y ShapedLinked List

Example 2:
Input: 
Linked List 1 = 4->1->common
Linked List 2 = 5->6->1->common
common = 8->4->5->NULL
Output: 8
Explanation: 

4              5
|              |
1              6
 \             /
  8   -----  1 
   |
   4
   |
  5
  |
  NULL    
  

Your Task:
You don't need to read input or print anything. The task is to complete the function intersectPoint() which takes the pointer to the head of linklist1(head1) and linklist2(head2) as input parameters and returns data value of a node where two linked lists intersect. If linked list do not merge at any point, then it should return -1.
Challenge : Try to solve the problem without using any extra space.


Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)


Constraints:
Length of Both linkedList before intersection(if any) is greater than 0.
2 ≤ N + M ≤ 2*10^5
-1000 ≤ value ≤ 1000
*/

// SOLUTION

/* Node of a linked list
 class Node {
   int data;
    Node next;
    Node(int d)  { data = d;  next = null; }
}
 Linked List class
class LinkedList
{
    Node head;  // head of list
}*/

// Brute Force
// Time Complexity: O(m*n), where m and n are number of nodes in two linked list.
// Auxiliary Space: O(1), Constant Space is used.
public Node getIntersectionNode(Node head1, Node head2) {
    while (head2 != null) {
        Node temp = head1;
        while (temp != null) {
            // if both Nodes are same
            if (temp == head2) {
                return head2;
            }
            temp = temp.next;
        }
        head2 = head2.next;
    }
    // If intersection is not present between the lists,
    // return NULL.
    return null;
}

// Better
// Time Complexity: O(n)
// Auxiliary Space: O(n)
public static Node MegeNode(Node n1, Node n2) {
    // define hashset
    HashSet<Node> hs = new HashSet<Node>();
    while (n1 != null) {
        hs.add(n1);
        n1 = n1.next;
    }
    while (n2 != null) {
        if (hs.contains(n2)) {
            return n2;
        }
        n2 = n2.next;
    }
    return null;
}

class Intersect {
    // Function to find intersection point in Y shaped Linked Lists.
    int intersectPoint(Node head1, Node head2) {
        Node a = head1;
        Node b = head2;

        while (a != b) {
            if (a != null) {
                a = a.next;
            } else {
                a = head2;
            }

            if (b != null) {
                b = b.next;
            } else {
                b = head1;
            }
        }
        if (a != null) {
            return a.data;
        }

        return -1;

        // -------------------------------

        // Same approach but different way
        Node ptr1 = head1;
        Node ptr2 = head2;

        // If any one of head is null i.e
        // no Intersection Point
        if (ptr1 == null || ptr2 == null) {

            return null;
        }

        // Traverse through the lists until they
        // reach Intersection node
        while (ptr1 != ptr2) {

            ptr1 = ptr1.next;
            ptr2 = ptr2.next;

            // If at any node ptr1 meets ptr2, then it is
            // intersection node.Return intersection node.

            if (ptr1 == ptr2) {

                return ptr1;
            }
            /*
             * Once both of them go through reassigning,
             * they will be equidistant from the collision point.
             */

            // When ptr1 reaches the end of a list, then
            // reassign it to the head2.
            if (ptr1 == null) {

                ptr1 = head2;
            }
            // When ptr2 reaches the end of a list, then
            // redirect it to the head1.
            if (ptr2 == null) {

                ptr2 = head1;
            }
        }

        return ptr1;
    }
}
