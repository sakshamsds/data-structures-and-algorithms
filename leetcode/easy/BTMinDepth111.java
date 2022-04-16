package easy;

import java.util.LinkedList;
import java.util.Queue;

import ds.TreeNode;

public class BTMinDepth111 {
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

        System.out.println(minDepth(root));
    }

    public static int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        // BFS
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int minDepth = 0;

        while (!q.isEmpty()) {
            minDepth++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                // if leaf node found
                if (node.left == null && node.right == null) {
                    return minDepth;
                }
                if (node.left != null) {
                    q.offer(node.left);
                }

                if (node.right != null) {
                    q.offer(node.right);
                }
            }
        }

        return minDepth;
    }
}
