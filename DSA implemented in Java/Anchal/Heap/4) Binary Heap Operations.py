"""
Binary Heap Operations

Medium

A binary heap is a Binary Tree with the following properties:
1) Its a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at the root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.

You are given an empty Binary Min Heap and some queries and your task is to implement the three methods insertKey,  deleteKey,  and extractMin on the Binary Min Heap and call them as per the query given below:
1) 1  x  (a query of this type means to insert an element in the min-heap with value x )
2) 2  x  (a query of this type means to remove an element at position x from the min-heap)
3) 3  (a query like this removes the min element from the min-heap and prints it ).

Example 1:
Input:
Q = 7
Queries:
insertKey(4)
insertKey(2)
extractMin()
insertKey(6)
deleteKey(0)
extractMin()
extractMin()
Output: 2 6 - 1
Explanation: In the first test case for
query 
insertKey(4) the heap will have  {4}  
insertKey(2) the heap will be {2 4}
extractMin() removes min element from 
             heap ie 2 and prints it
             now heap is {4} 
insertKey(6) inserts 6 to heap now heap
             is {4 6}
deleteKey(0) delete element at position 0
             of the heap,now heap is {6}
extractMin() remove min element from heap
             ie 6 and prints it  now the
             heap is empty
extractMin() since the heap is empty thus
             no min element exist so -1
             is printed.

             
Example 2:
Input:
Q = 5
Queries:
insertKey(8)
insertKey(9)
deleteKey(1)
extractMin()
extractMin()
Output: 8 -1
Your Task:
You are required to complete the 3 methods insertKey() which take one argument the value to be inserted, deleteKey() which takes one argument the position from where the element is to be deleted and extractMin() which returns the minimum element in the heap(-1 if the heap is empty)

Expected Time Complexity: O(Q*Log(size of Heap) ).
Expected Auxiliary Space: O(1).

Constraints:
1 <= Q <= 10^4
1 <= x <= 10^4

"""

# SOLUTION

'''
heap = [0 for i in range(101)]  # our heap to be used
'''

# Function to get the left child position of a node in the heap
def left(pos):
    return 2 * pos + 1

# Function to get the right child position of a node in the heap
def right(pos):
    return 2 * pos + 2

# Function to get the parent position of a node in the heap
def parent(pos):
    return (pos - 1) // 2

# Function to swap elements at two positions in the heap
def swap(pos1, pos2):
    global heap
    heap[pos1], heap[pos2] = heap[pos2], heap[pos1]

# Function to check if a node is a leaf node
def isLeaf(pos):
    if left(pos) > (curr_size - 1):
        return True
    return False

# Function to heapify the tree from top to bottom starting at a given position
def heapifyT2B(pos):
    if not isLeaf(pos):
        smallest = pos
        if heap[smallest] > heap[left(pos)]:
            smallest = left(pos)
        if heap[smallest] > heap[right(pos)]:
            smallest = right(pos)
        if smallest != pos:
            swap(smallest, pos)
            heapifyT2B(smallest)

# Function to heapify the tree from bottom to top starting at a given position
def heapifyB2T(pos):
    if pos > 0:
        if heap[pos] < heap[parent(pos)]:
            swap(pos, parent(pos))
            heapifyB2T(parent(pos))

# Function to decrease the key at a specific position in the heap
def decreaseKey(pos, val):
    global heap
    if val > heap[pos]:
        return False
    heap[pos] = val
    heapifyB2T(pos)
    return True

# Function to insert a value into the heap
def insertKey(x):
    global curr_size, heap
    if curr_size > 100:
        return False
    heap[curr_size] = x
    curr_size += 1
    heapifyB2T(curr_size - 1)

# Function to delete the key at a specific index in the heap
def deleteKey(i):
    global curr_size
    if i >= curr_size:
        return -1
    # Set the key at index i to a very small value
    decreaseKey(i, -9223372036854775806)
    # Extract the minimum value from the heap
    extractMin()

# Function to extract the minimum value from the heap
def extractMin():
    global heap, curr_size
    if curr_size == 0:
        return -1
    # Get the top element (minimum value) from the heap
    top_ele = heap[0]
    # Replace the root with the last element in the heap
    heap[0] = heap[curr_size - 1]
    curr_size -= 1
    # Heapify the tree from top to bottom starting at the root
    heapifyT2B(0)
    return top_ele