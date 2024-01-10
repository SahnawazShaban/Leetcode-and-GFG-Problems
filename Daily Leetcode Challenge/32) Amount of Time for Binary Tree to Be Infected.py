"""
2385. Amount of Time for Binary Tree to Be Infected

Medium

You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

 
Example 1:
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

Example 2:
Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^5
Each node has a unique value.
A node with a value of start exists in the tree.

"""


# Solution 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Queue to store infected nodes
        infectedNodesQueue = deque()

        # Function to add parent link to each node and enqueue the starting node
        def addParentLink(node, parent):
            if not node:
                return
            node.parent = parent
            addParentLink(node.left, node)
            addParentLink(node.right, node)

            # Enqueue the starting node if its value matches the specified 'start'
            if node.val == start:
                infectedNodesQueue.append(node)

        # Initial setup by adding parent links
        addParentLink(root, None)

        # Variable to store the time taken to infect all nodes
        timeTakenToInfect = 0

        # BFS to infect nodes and calculate time
        while infectedNodesQueue:
            currentInfectedCount = len(infectedNodesQueue)
            for i in range(currentInfectedCount):
                # Dequeue the current infected node
                currentNode = infectedNodesQueue.popleft()
                currentNode.val *= -1  # Marking the node as infected

                # Enqueue neighboring nodes if they are not infected
                if currentNode.left and currentNode.left.val > 0:
                    infectedNodesQueue.append(currentNode.left)
                if currentNode.right and currentNode.right.val > 0:
                    infectedNodesQueue.append(currentNode.right)
                if currentNode.parent and currentNode.parent.val > 0:
                    infectedNodesQueue.append(currentNode.parent)

            # If there are still infected nodes, increment the time taken
            if infectedNodesQueue:
                timeTakenToInfect += 1

        # Return the total time taken to infect all nodes
        return timeTakenToInfect


'''
Time Complexity:
The time complexity of the code is determined by the BFS traversal of the tree. In the worst case, each node in the tree needs to be processed once. The BFS loop processes each node and its neighbors, and the while loop continues until the queue is empty.

Let N be the number of nodes in the tree.

BFS Traversal: O(N)
Each node is processed once.
Overall, the time complexity is O(N).

Space Complexity:
The space complexity is determined by the space required for the queue during BFS traversal and the recursive call stack during the tree traversal.

Let h be the height of the tree (maximum depth of the recursive calls).

Queue Space: O(N/2) (in the worst case, the last level of the tree might require N/2 space in the queue)
Recursive Call Stack: O(h)
Overall, the space complexity is O(max(N/2, h)). In a balanced tree, the height h is log(N), so the space complexity is O(log(N)). In the worst case of an unbalanced tree, the height h can be equal to N, resulting in a space complexity of O(N).
'''
