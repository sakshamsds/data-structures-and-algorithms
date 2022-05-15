package medium;

import java.util.LinkedList;
import java.util.Queue;

import ds.TreeNode;
import ds.TreeNodeConversion;

public class DeepestLeavesSum1302 {
    public static void main(String[] args) {
        // int[] root = new int[] { 1, 2, 3, 4, 5, -1, 6, 7, -1, -1, -1, -1, 8 };
        int[] root = new int[] { 6, 7, 8, 2, 7, 1, 3, 9, -1, 1, 4, -1, -1, -1, 5 };
        System.out.println(new DeepestLeavesSum1302().deepestLeavesSum(TreeNodeConversion.convert(root)));
    }

    public int deepestLeavesSum(TreeNode root) {
        // level order traversal
        int sum = 0;
        boolean isDeepest = true;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            sum = 0;
            isDeepest = true;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                if (isDeepest) {
                    sum += node.val;
                } 
                if (node.left != null) {
                    q.offer(node.left);
                    isDeepest = false;
                }
                if (node.right != null) {
                    q.offer(node.right);
                    isDeepest = false;
                }
            }

        }

        return sum;
    }
}
