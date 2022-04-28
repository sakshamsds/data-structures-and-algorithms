package easy;

import java.util.LinkedList;
import java.util.Queue;

import ds.TreeNode;

public class SumOfLeftLeaves404 {
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

        System.out.println(new SumOfLeftLeaves404().sumOfLeftLeaves(root));
    }

    public int sumOfLeftLeaves(TreeNode root) {
        int sum = 0;
        if (root == null) {
            return sum;
        }

        // BFS
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode current = q.poll();
                // if current.left == leaf node then add to sum
                if (current.left != null) {
                    // check if leaf node else add to q
                    if (current.left.left == null && current.left.right == null) {
                        sum += current.left.val;
                    } else {
                        q.offer(current.left);
                    }
                }

                if (current.right != null) {
                    q.offer(current.right);
                }
            }
        }

        return sum;
    }
}
