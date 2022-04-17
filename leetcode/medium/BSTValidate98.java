package medium;

import java.util.Stack;

import ds.TreeNode;

// https://leetcode.com/problems/validate-binary-search-tree/submissions/
// 98. Validate Binary Search Tree

public class BSTValidate98 {
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

        // System.out.println(Integer.MIN_VALUE);
        // System.out.println(Integer.MAX_VALUE);

        System.out.println(isValidBST(root));
    }

    // iterative, in order traversal
    // another solution is to iterate in order and check for sorted array
    public static boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        Stack<TreeNode> stack = new Stack<>();
        TreeNode prev = null;
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (prev != null && root.val <= prev.val) {
                return false;
            }
            prev = root;
            root = root.right;
        }
        return true;
    }

    // // O(N)
    // public static boolean isValidBST(TreeNode root) {
    // long min = Long.MIN_VALUE;
    // long max = Long.MAX_VALUE;

    // return isValidBSTHelper(root, min, max);
    // }

    // public static boolean isValidBSTHelper(TreeNode root, long min, long max) {
    // if (root == null) {
    // return true;
    // }

    // if (root.val >= max || root.val <= min) {
    // return false;
    // }

    // return isValidBSTHelper(root.left, min, root.val) &&
    // isValidBSTHelper(root.right, root.val, max);
    // }

    // // for every node, check values in left subtree, then check values for right
    // // subtree, highly complex, O(n^2)
    // public static boolean isValidBST(TreeNode root) {
    // if (root == null) {
    // return true;
    // }

    // // BFS
    // Queue<TreeNode> q = new LinkedList<>();
    // q.offer(root);

    // while (!q.isEmpty()) {
    // int size = q.size();
    // for (int i = 0; i < size; i++) {
    // TreeNode node = q.poll();
    // // System.out.println(node.val);
    // boolean valid = isGreaterThanLeftSubTree(node.left, node.val)
    // && isSmallerThanRightSubTree(node.right, node.val);
    // if (!valid) {
    // return false;
    // }

    // if (node.left != null) {
    // q.offer(node.left);
    // }
    // if (node.right != null) {
    // q.offer(node.right);
    // }
    // }
    // }

    // return true;
    // }

    // public static boolean isGreaterThanLeftSubTree(TreeNode root, int val) {
    // if (root == null) {
    // return true;
    // }
    // if (root.val >= val) {
    // return false;
    // }
    // return isGreaterThanLeftSubTree(root.left, val) &&
    // isGreaterThanLeftSubTree(root.right, val);
    // }

    // public static boolean isSmallerThanRightSubTree(TreeNode root, int val) {
    // if (root == null) {
    // return true;
    // }
    // if (root.val <= val) {
    // return false;
    // }
    // return isSmallerThanRightSubTree(root.left, val) &&
    // isSmallerThanRightSubTree(root.right, val);
    // }

}
