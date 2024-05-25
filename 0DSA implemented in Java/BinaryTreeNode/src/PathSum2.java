import org.w3c.dom.ls.LSException;

import java.util.LinkedList;
import java.util.List;

public class PathSum2 {
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
        public static PathSum2.Node buildTree(int[] nodes){
            idx++;
            if(nodes[idx] == -1){
                return null;
            }

            PathSum2.Node newNode = new PathSum2.Node(nodes[idx]);
            newNode.left = buildTree(nodes);
            newNode.right = buildTree(nodes);

            return newNode;
        }
    }

    public static void hasPathSum(Node root, int targetSum, List<List<Integer>> res,List<Integer> smallAns){

        if (root == null){
            return;
        }
        if (root.left == null && root.right == null){
            if (targetSum - root.data == 0){
                List<Integer> base = new LinkedList<>(smallAns);
                base.add(root.data);
                res.add(base);
            }
            return;
        }
        smallAns.add(root.data);

        hasPathSum(root.left, targetSum- root.data, res, smallAns);
        hasPathSum(root.right, targetSum- root.data, res, smallAns);

        smallAns.remove(smallAns.size()-1);
    }


    public static List<List<Integer>> pathSum(Node root, int targetSum){
        List<List<Integer>> res = new LinkedList<>();
        List<Integer> smallAns = new LinkedList<>();

        hasPathSum(root,targetSum,res,smallAns);

        return res;
    }
    public static void main(String[] args) {
        int[] nodes = {7,3,1,4,-1,-1,0,-1,-1,-1,12,9,-17,-1,-1,-27,10,-1,-1,-1,13,15,-1,14,-1,-1,-1};
//        PathSum2.BinaryTree tree = new PathSum2.BinaryTree();
        PathSum2.Node root = BinaryTree.buildTree(nodes);

        List<List<Integer>> ans = pathSum(root,11);

        System.out.println(ans);
    }
}
