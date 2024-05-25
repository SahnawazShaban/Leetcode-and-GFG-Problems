import java.util.Queue;
import java.util.Scanner;

class QueueLL {
    static class Node{
        int val;
        Node next;

        Node(int val){
            this.val = val;
            this.next = null;
        }
    }
    Node f = null;
    Node r = null;

    public void enqueue(Scanner sc){
        System.out.println("Enter your data : ");
        int data = sc.nextInt();
        Node newNode = new Node(data);
        if (f == null && r == null){
            f = newNode;
            r = newNode;
        }
        else {
            r.next = newNode;
            r = newNode;
        }
    }

    public void dequeue(){
        if (f == null){
            System.out.println("Queue is Empty.");
        }
        else {
            f = f.next;
        }
    }

    public void display(){
        Node temp = f;
        while (temp!=null){
            System.out.print(temp.val + " ");
            temp = temp.next;
        }
        System.out.println("null");
    }
}

public class QueueUsingLinkedList{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        QueueLL qu = new QueueLL();
        int l;

        do{
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Display");
            System.out.println("Choose your option");
            int d = sc.nextInt();

            switch (d){
                case 1:
                    qu.enqueue(sc);
                    break;
                case 2:
                    qu.dequeue();
                    break;
                case 3:
                    qu.display();
                    break;
                default:
                    System.out.println("Enter Valid number.");
            }
            System.out.println("Enter any number to continue.");
            System.out.println("Enter 0 to EXIT : ");
            l = sc.nextInt();
        }while (l!=0);
    }
}

