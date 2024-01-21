"""
Search a node in BST

Basic

Given a Binary Search Tree and a node value X, find if the node with value X is present in the BST or not.


Example 1:
Input:         2
                \
                 81 
               /    \ 
             42      87 
              \       \ 
               66      90 
              / 
            45
X = 87
Output: 1
Explanation: As 87 is present in the
given nodes , so the output will be 1.

Example 2:
Input:      6
             \ 
              8 
             / \ 
            7   9
X = 11
Output: 0
Explanation: As 11 is not present in 
the given nodes , so the output will
be 0.

Your Task:
You don't need to read input or print anything. Complete the function search()which returns true if the node with value x is present in the BSTelse returns false.

Expected Time Complexity: O(Height of the BST)
Expected Auxiliary Space: O(1).


Constraints:
1 <= Number of nodes <= 10^5

"""


# SOLUTION

class BST:
    
    #Function to search a node in BST.
    def search(self, node, x):
        if node == None:
            return 0
        
        if node.data == x:
            return 1
        
        if node.data < x:
            # Search in right part
            return self.search(node.right,x)
        else:
            # Search in left part
            return self.search(node.left,x)
        

'''
In the given Binary Search Tree (BST) class, the search function recursively looks for a node with value x. 
The time complexity of this search operation is O(log N) in the average case, where N is the number of nodes in the tree. 
However, in the worst case (unbalanced tree), the time complexity can be O(N).

The space complexity is O(h), where h is the height of the tree. 
In a balanced BST, the height is log N, resulting in a space complexity of O(log N). 
However, in the worst case (unbalanced tree), the height is N, leading to a space complexity of O(N).
'''
