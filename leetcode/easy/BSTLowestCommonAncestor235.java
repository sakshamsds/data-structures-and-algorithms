package easy;

import ds.TreeNode;

// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
// 235. Lowest Common Ancestor of a Binary Search Tree

public class BSTLowestCommonAncestor235 {
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

        System.out.println(lowestCommonAncestor(root, node3, node2).val);
    }

    public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (p.val > q.val) {
            return LCAHelper(root, q, p);
        } else {
            return LCAHelper(root, p, q);
        }
    }

    public static TreeNode LCAHelper(TreeNode root, TreeNode left, TreeNode right) {
        // left, root, right
        if (right.val < root.val) {
            return LCAHelper(root.left, left, right);
        } else if (left.val > root.val) {
            return LCAHelper(root.right, left, right);
        } else{
            return root;
        }
    }

    // public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p,
    // TreeNode q) {
    // // make two lists
    // // find ancestors of both
    // // last common ancestor is the LCA

    // // find ancestors of p
    // List<TreeNode> ancestors1 = new ArrayList<>();
    // findAncestors(root, p.val, ancestors1);
    // // ancestors1.forEach(node -> System.out.println(node.val));

    // // find ancestors of q
    // List<TreeNode> ancestors2 = new ArrayList<>();
    // findAncestors(root, q.val, ancestors2);
    // // ancestors2.forEach(node -> System.out.println(node.val));

    // ancestors1.retainAll(ancestors2);
    // return ancestors1.get(ancestors1.size() - 1);
    // }

    // public static void findAncestors(TreeNode root, int target, List<TreeNode>
    // ancestors) {
    // // base condition
    // ancestors.add(root);
    // if (root.val == target) {
    // return;
    // }
    // if (root.val > target) {
    // findAncestors(root.left, target, ancestors);
    // } else {
    // findAncestors(root.right, target, ancestors);
    // }
    // }
}
