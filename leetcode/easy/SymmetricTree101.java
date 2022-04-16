package easy;

import java.util.LinkedList;
import java.util.List;

import ds.TreeNode;

// 101. Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

public class SymmetricTree101 {
    public static void main(String[] args) {

        // TreeNode root = new TreeNode(1);
        // TreeNode node1 = new TreeNode(2);
        // TreeNode node2 = new TreeNode(3);
        // TreeNode node3 = new TreeNode(4);
        // TreeNode node4 = new TreeNode(5);
        // root.left = node1;
        // root.right = node2;
        // node1.left = node3;
        // node1.right = node4;

        TreeNode root = new TreeNode(1);
        TreeNode node1 = new TreeNode(2);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(3);
        root.left = node1;
        root.right = node2;
        node1.right = node3;
        node2.right = node4;

        // System.out.println(isSymmetric(root));

        System.out.println(isSymmetric2(root));

    }

    // recursive + space complexity
    public static boolean isSymmetric(TreeNode root) {
        // traverse twice from left side and right side, both list should be equal
        // O(N), both time and space

        List<Integer> list1 = new LinkedList<>();
        leftSideTraversal(root.left, list1);
        List<Integer> list2 = new LinkedList<>();
        rightSideTraversal(root.right, list2);

        System.out.println(list1.toString());
        System.out.println(list2.toString());

        for (int i = 0; i < list1.size(); i++) {
            if (list1.get(i) != list2.get(i)) {
                return false;
            }
        }

        return true;
    }

    public static void leftSideTraversal(TreeNode root, List<Integer> list1) {
        if (root == null) {
            list1.add(null);
            return;
        }
        list1.add(root.val);
        leftSideTraversal(root.left, list1);
        leftSideTraversal(root.right, list1);
    }

    public static void rightSideTraversal(TreeNode root, List<Integer> list2) {
        if (root == null) {
            list2.add(null);
            return;
        }
        list2.add(root.val);
        rightSideTraversal(root.right, list2);
        rightSideTraversal(root.left, list2);
    }

    public static boolean isSymmetric2(TreeNode root) {
        return (root == null) || isSymmetric2Helper(root.left, root.right);
    }

    public static boolean isSymmetric2Helper(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        }

        if (left == null || right == null) {
            return false;
        }

        if (left.val != right.val) {
            return false;
        }

        return isSymmetric2Helper(left.left, right.right) && isSymmetric2Helper(left.right, right.left);
    }
}
