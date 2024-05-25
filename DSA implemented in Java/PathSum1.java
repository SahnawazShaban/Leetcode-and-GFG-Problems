public class PathSum1 {
    public static class Node{
        int data;
        Node left;
        Node right;

        Node(int data){
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    static class BinaryTree{
        static int idx = -1;
        public static PathSum1.Node buildTree(int[] nodes){
            idx++;
            if(nodes[idx] == -1){
                return null;
            }

            PathSum1.Node newNode = new PathSum1.Node(nodes[idx]);
            newNode.left = buildTree(nodes);
            newNode.right = buildTree(nodes);

            return newNode;
        }
    }

    public static boolean hasPathSum(Node root,int targetSum){
        if (root == null){
            return false;
        }
        if (root.left == null && root.right == null){
            return (targetSum - root.data) == 0;
        }

        return hasPathSum(root.left,targetSum-root.data) || hasPathSum(root.right,targetSum-root.data);
    }

    public static void main(String[] args) {
        int[] nodes = {7,3,1,3,-1,-1,2,-1,-1,-1,12,9,-17,-1,-1,-27,10,-1,-1,-1,13,15,-1,14,-1,-1,-1};
//        PathSum1.BinaryTree sum = new PathSum1.BinaryTree();
        PathSum1.Node root = BinaryTree.buildTree(nodes);

        boolean ans = hasPathSum(root,11);

        System.out.println(ans);
    }
}
