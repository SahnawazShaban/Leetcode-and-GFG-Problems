class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}


public class StackUsingLinkedList {
    private Node top; // Points to the top of the stack

    // Constructor to initialize an empty stack
    public LinkedListStack() {
        this.top = null;
    }

    // Method to check if the stack is empty
    public boolean isEmpty() {
        return top == null;
    }

    // Method to push an element onto the stack
    public void push(int data) {
        Node newNode = new Node(data);
        newNode.next = top; // Link new node to the previous top
        top = newNode; // Set the new node as the top
    }

    // Method to pop an element from the stack
    public int pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        int data = top.data; // Get the data from the top node
        top = top.next; // Move top to the next node
        return data; // Return the popped data
    }

    // Method to peek the top element of the stack without removing it
    public int peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return top.data; // Return data of the top node
    }

    // Method to print the stack elements
    public void printStack() {
        Node current = top;
        System.out.print("Stack: ");
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    // Main method for testing
    public static void main(String[] args) {
        StackUsingLinkedList stack = new StackUsingLinkedList();

        // Pushing elements onto the stack
        stack.push(1);
        stack.push(2);
        stack.push(3);

        stack.printStack(); // Stack: 3 2 1

        // Popping an element from the stack
        System.out.println("Popped element: " + stack.pop()); // Popped element: 3

        stack.printStack(); // Stack: 2 1

        // Peeking the top element
        System.out.println("Top element: " + stack.peek()); // Top element: 2
    }
}
