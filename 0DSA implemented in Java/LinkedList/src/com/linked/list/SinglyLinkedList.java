package com.linked.list;

import java.util.List;
import java.util.stream.LongStream;

public class SinglyLinkedList {

    private ListNode head;

    private class ListNode { // this class is responsible for holding the data
        private int data;
        private ListNode next;

        public ListNode(int data){
           this.data = data;
           this.next = null;
        }
    }

    public void insertAtBeginning(int data){
        ListNode newNode = new ListNode(data);
        newNode.next = head;
        head = newNode;
    }

    public void dispay(){
        if (head == null){
            System.out.println("null");
        }
        ListNode current = head;
        while (current != null){
            System.out.print(current.data +  " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public ListNode getMiddleNode(ListNode head){
        if (head == null){
            return null;
        }
        ListNode slow = head;
        ListNode fast = head.next;

        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }

    public ListNode getNthNumberOfNode(int n){
        if (head == null){
            return null;
        }
        ListNode temp = head;

        for (int i=1;i<n;i++){
            temp = temp.next;
        }
        return temp;
    }

    public ListNode reverse(ListNode head){
        if (head == null){
            return null;
        }
        ListNode prev = null;
        ListNode cur = head;

        while (cur != null){
            ListNode forward = cur.next;
            cur.next = prev;
            prev = cur;
            cur = forward;
            System.out.print(prev.data + " -> ");
        }
        return prev;
    }

    public static void main(String[] args) {
        SinglyLinkedList sll = new SinglyLinkedList();

        sll.insertAtBeginning(2);
        sll.insertAtBeginning(3);
        sll.insertAtBeginning(6);
        sll.insertAtBeginning(12);
        sll.insertAtBeginning(15);
        sll.insertAtBeginning(4);

        sll.dispay();

        ListNode ans = sll.getMiddleNode(sll.head);
        System.out.println(ans.data);

        ListNode ans1 = sll.getNthNumberOfNode(5);
        System.out.println(ans1.data);

        ListNode ans2 = sll.reverse(sll.head);
        sll.dispay();

    }
}
