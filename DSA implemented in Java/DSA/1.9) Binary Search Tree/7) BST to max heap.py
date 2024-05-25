"""
BST to max heap

Medium

Given a Binary Search Tree. Convert a given BST into a Special Max Heap with the condition that all the values in the left subtree of a node should be less than all the values in the right subtree of the node. This condition is applied on all the nodes in the so converted Max Heap.

Example 1:
Input :
                 4
               /   \
              2     6
            /  \   /  \
           1   3  5    7  

Output : 1 2 3 4 5 6 7 
Exaplanation :
               7
             /   \
            3     6
          /   \  /   \
         1    2 4     5
The given BST has been transformed into a
Max Heap and it's postorder traversal is
1 2 3 4 5 6 7.

Your task :
You don't need to read input or print anything. Your task is to complete the function convertToMaxHeapUtil() which takes the root of the tree as input and converts the BST to max heap.
Note : The driver code prints the postorder traversal of the converted BST.
 
Expected Time Complexity : O(n)
Expected Auxiliary Space : O(n)
 
Constraints :
1 ≤ n ≤ 10^5

"""


# SOLUTION

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

class Solution:
    def convertToMaxHeapUtil(self, root):
        arr = []
        self.inorder(root, arr)
        arr = arr[::-1]
        self.postorder(root, arr)
        
        return root
        
    def inorder(self, root, arr):
        if root == None:
            return 
        
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)
        
    
    def postorder(self, root, arr):
        if root == None:
            return 
        
        self.postorder(root.left, arr)
        self.postorder(root.right, arr)
        root.data = arr.pop()


'''
Time Complexity:
In the inorder and postorder functions, each node is processed once. The time complexity for both is O(N), where N is the number of nodes in the binary tree.
Reversing the array (arr[::-1]) takes O(N) time.
The overall time complexity is O(N).

Space Complexity:
The arr list is used to store the values of the nodes during the in-order traversal. In the worst case, where the tree is completely skewed, the space complexity would be O(N), as all nodes need to be stored.
The space used by the call stack during recursive calls is proportional to the height of the tree. In the worst case, for a skewed tree, it would be O(N).
'''