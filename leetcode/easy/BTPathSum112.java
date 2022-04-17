package easy;

import java.util.LinkedList;
import java.util.Queue;

import ds.TreeNode;

// https://leetcode.com/problems/path-sum/
// 112. Path Sum

public class BTPathSum112 {
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

        int targetSum = 4;
        System.out.println(hasPathSum(root, targetSum));
    }

    public static boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return false;
        }

        //BFS
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                // leaf node
                if (node.left == null && node.right == null && node.val == targetSum) {
                    return true;
                }

                if (node.left != null) {
                    node.left.val += node.val;
                    q.offer(node.left);
                }
                if (node.right != null) {
                    node.right.val += node.val;
                    q.offer(node.right);
                }
            }
        }

        return false;
    }

}
