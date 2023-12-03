"""
Singly Linked List

- Traverse Linked List

- Add begin
- Add end
- Add After x element
- Add Before x element
- Add between with count

- Delete begin
- Delete end
- Delete in between
- Delete by value

"""

# SOLUTION

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head is None:
            print("Linked List is Empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data,"->",end=" ")
                n = n.next
            print("Null")

    def add_begin(self,data):
        new_node = Node(data)

        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)

        if self.head:
            n = self.head
            while n.next != None:
                n = n.next
            n.next = new_node
            # new_node.next = None
        else:
            self.head = new_node

    def add_after_x(self,data,x):
        new_node = Node(data)
        if self.head:
            n = self.head
            while n.data != x:
                n = n.next
            new_node.next = n.next
            n.next = new_node
        else:
            self.head = new_node

    def add_before_x(self,data,x):
        new_node = Node(data)

        if self.head:
            n = self.head
            while n.next.data != x:
                n = n.next
            new_node.next = n.next
            n.next = new_node
        else:
            self.head = new_node

    def add_between_with_count(self,data,count):
        new_node = Node(data)

        if self.head:
            temp_count = 1
            n = self.head
            while temp_count != count:
                temp_count += 1
                n = n.next
            new_node.next = n.next
            n.next = new_node
        else:
            self.head = new_node

    def delete_begin(self):
        if self.head:
            self.head = self.head.next
        else:
            print("Linked List empty.")

    def delete_end(self):
        if self.head == None:
            print("Linked List is empty.")
        elif self.head.next == None:
            self.head = None
        else:
            n = self.head
            while n.next.next != None:
                n = n.next
            n.next = None

    def delete_inbetween(self,x):
        if self.head:
            temp = 1
            n = self.head
            while temp != x-1:
                n = n.next
                temp += 1
            n.next = n.next.next
        else:
            print("Linked List is empty.")

    def delete_by_value(self,val):
        if self.head:
            n = self.head
            while n.next.data != val:
                n = n.next
            n.next = n.next.next
        else:
            print("Linked List is empty.")


LL = LinkedList()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(30)
LL.add_begin(40)
LL.add_end(50)
LL.add_after_x(90,20)
LL.add_before_x(125,90)
LL.add_between_with_count(141,3)
LL.delete_begin()
LL.delete_end()
LL.delete_inbetween(3)
LL.delete_by_value(125)
LL.delete_end()
LL.delete_end()
LL.delete_end()
LL.delete_end()
LL.printLL()

# IF YOU HAVE ANY QUESTIONS, PLEASE ASK ME.

