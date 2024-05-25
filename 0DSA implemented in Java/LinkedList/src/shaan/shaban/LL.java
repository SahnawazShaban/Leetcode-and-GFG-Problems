package shaan.shaban;

public class LL {
    private Node head;
    private Node tail;
    private int size;

    public LL(){
        this.size = 0;
    }
    public void insertFirst(int val){
        Node node = new Node(val);
        node.next = head;
        head = node;

        if (tail == null){
            tail = head;
        }
        size++;
    }

    public void insertLast(int val){
        if (tail == null){
            insertFirst(val);
            return;
        }
        Node node = new Node(val);
        tail.next = node;
        tail = node;
        size++;
    }

    public void insert(int val,int index){
        if (index == 0){
            insertFirst(val);
            return;
        }
        if (index == size){
            insertLast(val);
            return;
        }

        Node temp = head;
        for (int i=1;i<index;i++){
            temp = temp.next;
        }
        Node node = new Node(val,temp.next);
        node.next = temp.next;
        temp.next = node;
        size++;
    }

    public int deleteFirst(){
        int val = head.value;
        head = head.next;
        if (head == null){
            tail = null;
        }
        size--;
        return val;
    }

    public  int deleteLast(){
        if (size <= 1){
            return deleteFirst();
        }

        Node secondLast = get(size-2);

        int val = tail.value;
        tail = secondLast;
        tail.next = null;

        return val;
    }
    public int delete(int index){
        if (index == 0){
            return deleteFirst();
        }
        if (index == size-1){
            return deleteLast();
        }
        Node prev = get(index-1);
        int val = prev.next.value;
        prev.next = prev.next.next;
        return val;
    }

    public Node get(int index){
        Node node = head;
        for (int i=0;i<index;i++){
            node = node.next;
        }
        return node;
    }

    public void display(){
        Node temp = head;

        while (temp != null){
            System.out.print(temp.value+" --> ");
            temp = temp.next;
        }
        System.out.println("NULL");
    }

    public Node find(int value){
        Node node = head;
        while (node != null){
            if (node.value == value){
                return node;
            }
            node = node.next;
        }
        return null; // if u nothing is find, then return null
    }
    private class Node{
        private int value;
        private Node next;

        public Node(int value){
            this.value = value;
        }

        public Node(int value,Node next){
            this.value = value;
            this.next = next;
        }

        public void display() {
            Node temp = head;

            while (temp != null){
                System.out.print(temp.value+" --> ");
                temp = temp.next;
            }
            System.out.println("NULL");
        }
    }

    //questions

    //Remove Duplicate from sorted linked list

    public void duplicate(){
        Node node = head;
        while (node.next != null){
            if (node.value == node.next.value){
                node.next = node.next.next;
                size--; // skip a particular number size will also decrease
            }
            else {
                node = node.next;
            }
        }
        tail = node;
        tail.next = null;
    }

    public static LL merge(LL first,LL second){
        Node f = first.head;
        Node s = second.head;

        LL ans = new LL();

        while (f != null && s !=null){
            if (f.value < s.value){
                ans.insertLast(f.value);
                f = f.next;
            }
            else {
                ans.insertLast(s.value);
                s = s.next;
            }
        }

        while (f != null){
            ans.insertLast(f.value);
            f = f.next;
        }
        while (s != null){
            ans.insertLast(s.value);
            s = s.next;
        }
        return ans;
    }

    public static Node removeElements(Node head, int val) {
        while(head != null && head.value == val){ // node : 3,3,3,3,5,6,2,3,3 : val = 3
            head = head.next;
        }

        if(head == null){
            return head;
        }

        Node temp = head;

        while(temp.next != null){
            if(temp.next.value == val){
                temp.next = temp.next.next;
                System.out.println(temp.value + " ");
            }
            else{
                temp = temp.next;
            }
        }

        return head;
    }
    public static void main(String[] args) {
//        LL dup = new LL();
//        dup.insertLast(1);
//        dup.insertLast(1);
//        dup.insertLast(1);
//        dup.insertLast(2);
//        dup.insertLast(2);
//        dup.insertLast(3);
//        dup.insertLast(3);
//
//        dup.display();
//        dup.duplicate();
//        dup.display();

        LL first = new LL();
        LL second  = new LL();

        first.insertLast(1);
        first.insertLast(2);
        first.insertLast(3);
        first.insertLast(3);
        first.insertLast(3);
        first.insertLast(4);
        first.insertLast(3);

        second.insertLast(1);
        second.insertLast(3);
        second.insertLast(5);
        second.insertLast(8);
        second.insertLast(9);

        System.out.println("Before Remove Element : ");
        first.display();

        System.out.println("After Remove Element : ");
        Node result = LL.removeElements(first.head, 3);
        result.display();

//        LL ans = LL.merge(first,second);
//        ans.display();
    }
}
