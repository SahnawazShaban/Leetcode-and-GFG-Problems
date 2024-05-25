"""
Huffman Encoding

Medium

Given a string S of distinct character of size N and their corresponding frequency f[ ] i.e. character S[i] has f[i] frequency. Your task is to build the Huffman tree print all the huffman codes in preorder traversal of the tree.
Note: While merging if two nodes have the same value, then the node which occurs at first will be taken on the left of Binary Tree and the other one to the right, otherwise Node with less value will be taken on the left of the subtree and other one to the right.

Example 1:
S = "abcdef"
f[] = {5, 9, 12, 13, 16, 45}
Output: 
0 100 101 1100 1101 111
Explanation:
Steps to print codes from Huffman Tree
HuffmanCodes will be:
f : 0
c : 100
d : 101
a : 1100
b : 1101
e : 111
Hence printing them in the PreOrder of Binary
Tree.
Your Task:
You don't need to read or print anything. Your task is to complete the function huffmanCodes() which takes the given string S, frequency array f[ ] and number of characters N as input parameters and returns a vector of strings containing all huffman codes in order of preorder traversal of the tree.

Expected Time complexity: O(N * LogN)
Expected Space complexity: O(N)

Constraints:
1 ≤ N ≤ 26

"""

# SOLUTION

import heapq

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        
    # The priority queue uses the __lt__ method of the Node class to compare the frequencies and maintain the heap property.
    
    def __lt__(self, other):
        return self.data < other.data

class Solution:
    def traverse(self, root, ans, temp):
        # Recursive function to traverse the Huffman tree and generate codes
        if not root.left and not root.right:
            ans.append(temp)  # Leaf node reached, add the generated code to the result
            return

        if root.left:
            self.traverse(root.left, ans, temp + '0')  # Traverse left subtree with '0' appended to the code
        if root.right:
            self.traverse(root.right, ans, temp + '1')  # Traverse right subtree with '1' appended to the code

    def huffmanCodes(self, S, f, N):
        pq = []
        # Initialize a priority queue with nodes containing frequencies and characters
        for i in range(N):
            temp = Node(f[i])
            heapq.heappush(pq, (temp.data, temp))

        # Build the Huffman tree
        while len(pq) > 1:
            # Extract two nodes with the lowest frequencies from the priority queue
            left = heapq.heappop(pq)[1]
            right = heapq.heappop(pq)[1]

            # Create a new internal node with a frequency equal to the sum of its children
            new_node = Node(left.data + right.data)
            new_node.left = left
            new_node.right = right

            # Add the new internal node back to the priority queue
            heapq.heappush(pq, (new_node.data, new_node))

        root = pq[0][1]
        ans = []
        temp = ""
        self.traverse(root, ans, temp)  # Generate Huffman codes by traversing the tree
        return ans
    

'''
Time Complexity:
Building Priority Queue (Min Heap): Constructing the priority queue by inserting N nodes (where N is the number of characters in the input) has a time complexity of O(N * log N). Each insertion operation in a binary heap (used as a priority queue) takes O(log N) time, and there are N insertions.
Building Huffman Tree: The process of combining nodes in the priority queue to build the Huffman tree takes O(N * log N) time, as each iteration involves extracting two nodes and inserting one new node back into the priority queue.
Therefore, the overall time complexity of the Huffman coding algorithm is O(N * log N).

Space Complexity:
Priority Queue: The space complexity for the priority queue is O(N), as it stores N nodes representing the characters in the input.
Huffman Tree: The space complexity for the Huffman tree is O(N), as it also stores N nodes.
Output: The space required to store the output Huffman codes is O(N), where N is the number of characters.
The overall space complexity is O(N).
'''