/*
206. Reverse Linked List
Easy
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
*/

// SOLUTION

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {

    //SOLUTION 1

    // ListNode temp = null;

    // while(head != null){
    //     ListNode Next = head.next;
    //     head.next = temp;
    //     temp = head;
    //     head = Next;
    // }
    // return temp;

    //SOLUTION 2

    ListNode cur = head;
    ListNode prev = null;

    while(cur != null){
        ListNode temp = cur.next;
        cur.next = prev;
        prev = cur;
        cur = temp;
    }

    return prev;
}
}
// ------------------------------

/* Recursive Solution */
class Solution{
    public ListNode reverseList(ListNode head) {
        return reverse(head, null);
    }
    
    private ListNode reverse(ListNode cur, ListNode prev) {
        if (cur == null)
            return prev;
        ListNode temp = cur.next;
        cur.next = prev;
        return reverse(temp, cur);
    }
}
// null<-1<-2<-3
//               c  n
//             p