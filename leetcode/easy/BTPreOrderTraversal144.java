package easy;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import ds.TreeNode;

// 144. Binary Tree Preorder Traversal
// https://leetcode.com/problems/binary-tree-preorder-traversal/

public class BTPreOrderTraversal144 {
    public static void main(String[] args) {
        /**
         *          1
         *      2       3
         *   4      5
         */
        TreeNode root = new TreeNode(1);
        TreeNode node1 = new TreeNode(2);
        TreeNode node2 = new TreeNode(3);
        TreeNode node3 = new TreeNode(4);
        TreeNode node4 = new TreeNode(5);
        root.left = node1;
        root.right = node2;
        node1.left = node3;
        node1.right = node4;

        System.out.println(preorderTraversal(root).toString());
    }

    // inorder -> left, root, right
    // preorder -> root, left, right
    // postorder -> left, right, root
    public static List<Integer> preorderTraversal(TreeNode root) {

        // recursive
        // List<Integer> output = new ArrayList<>();

        // if(root == null){
        // return output;
        // }

        // output.add(root.val);
        // output.addAll(preorderTraversal(root.left));
        // output.addAll(preorderTraversal(root.right));
        // return output;

        // iterative usually better to avoid stack overflow exceptions
        List<Integer> output = new ArrayList<>();
        if (root == null) {
            return output;
        }
        Stack<TreeNode> toVisit = new Stack<>();
        toVisit.push(root);
        while (!toVisit.empty()) {
            TreeNode visiting = toVisit.pop();
            output.add(visiting.val);

            // push right first, so when we pop, left gets priority
            if (visiting.right != null) {
                toVisit.push(visiting.right);
            }
            if (visiting.left != null) {
                toVisit.push(visiting.left);
            }
        }
        return output;
    }
}
