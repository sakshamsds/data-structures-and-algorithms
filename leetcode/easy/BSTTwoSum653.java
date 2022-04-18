package easy;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

import ds.TreeNode;

// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
// 653. Two Sum IV - Input is a BST

public class BSTTwoSum653 {
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

        System.out.println(findTarget(root, 11));
    }

    public static boolean findTarget(TreeNode root, int k) {
        // BFS
        if (root == null) {
            return false;
        }
        Set<Integer> set = new HashSet<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                if (set.contains(node.val)) {
                    return true;
                } else {
                    set.add(k - node.val);
                }
                if (node.left != null) {
                    q.offer(node.left);
                }
                if (node.right != null) {
                    q.offer(node.right);
                }
            }
        }

        return false;
        // Set<Integer> set = new HashSet<>();

        // // O(N)
        // // in order traversal
        // Stack<TreeNode> stack = new Stack<>();
        // while (root != null || !stack.empty()) {
        // while (root != null) {
        // stack.push(root);
        // root = root.left;
        // }

        // root = stack.pop();
        // // O(1)
        // if (set.contains(root.val)) {
        // return true;
        // }
        // set.add(k - root.val);
        // root = root.right;
        // }

        // return false;
    }
}
