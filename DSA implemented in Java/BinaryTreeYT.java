import javax.swing.plaf.basic.BasicTreeUI;
import javax.swing.tree.TreeNode;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BinaryTreeYT {
    static class Node{
        int data;
        Node left;
        Node right;

        // Create Constructor
        Node(int data){
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }
    static class BinaryTree{
        static int idx = -1;
        public static Node buildTree(int[] nodes){
            idx++;
            if(nodes[idx] == -1){
                return null;
            }

            Node newNode = new Node(nodes[idx]);
            newNode.left = buildTree(nodes);
            newNode.right = buildTree(nodes);

            return newNode;
        }
    }
    public static void preorder(Node root){
        if (root == null){
            return;
        }
        System.out.print(root.data + " ");

        preorder(root.left);
        preorder(root.right);
    }

    public static void inorder(Node root){
        if (root == null){
            return;
        }
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);
    }

    public static void postorder(Node root){
        if (root == null){
            return;
        }
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.data + " ");
    }

    public static void levelOrder(Node root){
        if (root == null){
            return;
        }
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        queue.add(null);

        while (!queue.isEmpty()){
            Node currNode = queue.poll();

            if (currNode == null){
                System.out.println();
                if (queue.isEmpty()){
                    break;
                }
                else {
                    queue.add(null);
                }
            }
            else {
                System.out.print(currNode.data + " ");
                if (currNode.left != null){
                    queue.add(currNode.left);
                }
                if (currNode.right != null){
                    queue.add(currNode.right);
                }
            }
        }
    }

    public static int countNodes(Node root){
        if (root == null){
            return 0;
        }
        int leftNodes = countNodes(root.left);
        int rightNodes = countNodes(root.right);

        return leftNodes+rightNodes+1;
    }

    public static int sumOfNodes(Node root){
        if (root == null){
            return 0;
        }

        int leftSum = sumOfNodes(root.left);
        int rightSum = sumOfNodes(root.right);

        return leftSum + rightSum + root.data;
    }

    public static int height(Node root){
        if (root == null){
            return 0;
        }
        int leftHeight = height(root.left);
        int rightHeight = height(root.right);

        return Math.max(leftHeight,rightHeight) + 1;
    }

    public static int diameter(Node root){
        if (root == null){
            return 0;
        }

//        int dia1 = height(root.left);
//        int dia2 = height(root.right);
//        int dia3 = dia1+dia2;

        int dia1 = diameter(root.left);
        int dia2 = diameter(root.right);
        int dia3 = height(root.left)+height(root.right);

        return Math.max(dia3,Math.max(dia1,dia2)) + 1;
    }

    //har node ko apni height and diameter sath mein return karna hai
    //do return type toh nahi likh sakte.
    //dono ko ek sath iss class ke object ke through bhejna hai
    //Create TreeInfo and create 2 variable

    static class TreeInfo{
        int ht;
        int dia;

        TreeInfo(int ht,int dia){
            this.ht = ht;
            this.dia = dia;
        }
    }

    public static TreeInfo diameter2(Node root){
        if (root == null){
            return new TreeInfo(0,0);
        }
        TreeInfo left = diameter2(root.left);
        TreeInfo right = diameter2(root.right);

        int myHeight = Math.max(left.ht,right.ht) + 1;
        int dia1 = left.dia; //ls
        int dia2 = right.dia; //rs
        int dia3 = left.ht + right.ht + 1; //(ls+rs+1)

        int mydia = Math.max(dia3,Math.max(dia1,dia2));

//        TreeInfo myInfo = new TreeInfo(myHeight,mydia);
//
//        return myInfo;
//
//        OR

        return new TreeInfo(myHeight,mydia);
    }

    public static List<List<Integer>> levelOrder1(Node root){
        Queue<Node> queue = new LinkedList<>();

        List<List<Integer>> mainList = new LinkedList<>();
        if (root == null){
            return mainList;
        }

        queue.offer(root);

        while (!queue.isEmpty()){
            int size = queue.size();
            List<Integer> virtualList = new LinkedList<>();

            for (int i=0;i<size;i++){
                if (queue.peek().left != null){
                    queue.offer(queue.peek().left);
                }
                if (queue.peek().right != null){
                    queue.offer(queue.peek().right);
                }
                virtualList.add(queue.poll().data);
            }
            mainList.add(virtualList);
        }
        return mainList;
    }
    public static void main(String[] args) {
//        int[] nodes = {1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};
        int[] nodes = {1,2,4,-1,-1,5,6,-1,-1,-1,3,7,-1,-1,8,9,-1,-1,10,-1,-1};
        BinaryTree tree = new BinaryTree();
        Node root = tree.buildTree(nodes);

//        System.out.println(root.data);

//        System.out.println("Pre-Order Traversal");
//        preorder(root);
//
//        System.out.println();
//        System.out.println("In-Order Traversal");
//        inorder(root);
//
//        System.out.println();
//        System.out.println("Post-Order Traversal");
//        postorder(root);

//        System.out.println();
//        System.out.println("Level Order Traversal - 1 : ");
//        levelOrder(root);

        System.out.println();
        System.out.println("Count no. of Nodes");
        int ans = countNodes(root);
        System.out.println(ans);
//
//        System.out.println();
//        System.out.println("Sum of Nodes");
//        int ans1 = sumOfNodes(root);
//        System.out.println(ans1);
//
//        System.out.println();
//        System.out.println("Height of Tree");
//        int ans2 = height(root);
//        System.out.println(ans2);
//
//        System.out.println();
//        System.out.println("Diameter of Tree - 1");
//        System.out.println("Time Complexity : O(N2)");
//        int ans3 = diameter(root);
//        System.out.println(ans3);
//
//        System.out.println();
//        System.out.println("Diameter of Tree - 2");
//        System.out.println("Time Complexity : O(N)");
//        System.out.println(diameter2(root).dia);

        System.out.println();
        System.out.println("Level Order Traversal - 2 : ");
        System.out.println(levelOrder1(root));
    }
}
