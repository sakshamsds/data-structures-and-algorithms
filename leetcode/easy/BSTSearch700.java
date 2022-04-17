package easy;

import ds.TreeNode;

// https://leetcode.com/problems/search-in-a-binary-search-tree/
// 700. Search in a Binary Search Tree

public class BSTSearch700 {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(4);
        TreeNode node1 = new TreeNode(2);
        TreeNode node2 = new TreeNode(7);
        TreeNode node3 = new TreeNode(1);
        TreeNode node4 = new TreeNode(3);
        root.left = node1;
        root.right = node2;
        node1.left = node3;
        node1.right = node4;

        int val = 3;

        System.out.println(searchBST(root, val).val);

    }

    public static TreeNode searchBST(TreeNode root, int val) {
        // DFS is usually not efficient
        // O(H), h = height of tree, O(N) in balanced BST
        if (root == null || root.val == val) {
            return root;
        }

        if (root.val > val) {
            return searchBST(root.left, val);
        } else {
            return searchBST(root.right, val);
        }

    }

}
