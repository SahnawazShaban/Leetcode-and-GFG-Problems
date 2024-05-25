/*
Left View of Binary Tree

Easy

Given a Binary Tree, return Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    / \
  4     5   6    7
   \
     8   

Example 1:
Input:
   1
 /  \
3    2
Output: 1 3

Example 2:
Input:
Output: 10 20 40

Your Task:
You just have to complete the function leftView() that returns an array containing the nodes that are in the left view. The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
0 <= Number of nodes <= 100
1 <= Data of a node <= 1000

*/


// SOLUTION



// Java program to print left view of Binary
// Tree
import java.util.*;

public class PrintRightView {
	// Binary tree node
	private static class Node {
		int data;
		Node left, right;

		public Node(int data)
		{
			this.data = data;
			this.left = null;
			this.right = null;
		}
	}

	// function to print left view of binary tree
	private static void printLeftView(Node root)
	{
		if (root == null)
			return;

		Queue<Node> queue = new LinkedList<>();
		queue.add(root);

		while (!queue.isEmpty()) {
			// number of nodes at current level
			int n = queue.size();

			// Traverse all nodes of current level
			for (int i = 1; i <= n; i++) {
				Node temp = queue.poll();

				// Print the left most element at
				// the level
				if (i == 1)
					System.out.print(temp.data + " ");

				// Add left node to queue
				if (temp.left != null)
					queue.add(temp.left);

				// Add right node to queue
				if (temp.right != null)
					queue.add(temp.right);
			}
		}
	}

	// Driver code
	public static void main(String[] args)
	{
		// construct binary tree as shown in
		// above diagram
		Node root = new Node(10);
		root.left = new Node(2);
		root.right = new Node(3);
		root.left.left = new Node(7);
		root.left.right = new Node(8);
		root.right.right = new Node(15);
		root.right.left = new Node(12);
		root.right.right.left = new Node(14);

		printLeftView(root);
	}
}

// ---------------------------------------------------------------
// Java program to print left view of binary tree

/* Class containing left and right child of current
node and key value*/
class Node {
	int data;
	Node left, right;

	public Node(int item)
	{
		data = item;
		left = right = null;
	}
}

/* Class to print the left view */
class BinaryTree {
	Node root;
	static int max_level = 0;

	// recursive function to print left view
	void leftViewUtil(Node node, int level)
	{
		// Base Case
		if (node == null)
			return;

		// If this is the first node of its level
		if (max_level < level) {
			System.out.print(node.data + " ");
			max_level = level;
		}

		// Recur for left and right subtrees
		leftViewUtil(node.left, level + 1);
		leftViewUtil(node.right, level + 1);
	}

	// A wrapper over leftViewUtil()
	void leftView()
	{
		max_level = 0;
		leftViewUtil(root, 1);
	}

	/* testing for example nodes */
	public static void main(String args[])
	{
		/* creating a binary tree and entering the nodes */
		BinaryTree tree = new BinaryTree();
		tree.root = new Node(10);
		tree.root.left = new Node(2);
		tree.root.right = new Node(3);
		tree.root.left.left = new Node(7);
		tree.root.left.right = new Node(8);
		tree.root.right.right = new Node(15);
		tree.root.right.left = new Node(12);
		tree.root.right.right.left = new Node(14);

		tree.leftView();
	}
}
