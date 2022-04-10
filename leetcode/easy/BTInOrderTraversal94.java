package easy;

import java.util.ArrayList;
import java.util.List;

import ds.TreeNode;

// https://leetcode.com/problems/binary-tree-inorder-traversal/
// 94. Binary Tree Inorder Traversal

public class BTInOrderTraversal94 {

    public static void main(String[] args) {

        TreeNode root = new TreeNode(1);
        TreeNode node1 = new TreeNode(2);
        TreeNode node2 = new TreeNode(3);
        TreeNode node3 = new TreeNode(4);
        TreeNode node4 = new TreeNode(5);
        root.left = node1;
        root.right = node2;
        node1.left = node3;
        node1.right = node4;

        System.out.println(inorderTraversal(root));
    }

    // inorder, left, root, right
    // recursive
    public static List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> output = new ArrayList<>();
        if (root == null)
            return output;

        output.addAll(inorderTraversal(root.left));
        output.add(root.val);
        output.addAll(inorderTraversal(root.right));

        return output;
    }

}
