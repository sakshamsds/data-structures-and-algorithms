package ds;

import java.util.LinkedList;
import java.util.Queue;

import medium.BTLevelOrderTraversal102;

public class TreeNodeConversion {
    public static void main(String[] args) {
        int[] input = new int[] { 6, 7, 8, 2, 7, 1, 3, 9, -1, 1, 4, -1, -1, -1, 5 };
        // int[] input = new int[] { 1, 2, 3, 4, 5, -1, 6, 7, -1, -1, -1, -1, 8 };
        System.out.println(BTLevelOrderTraversal102.levelOrder(TreeNodeConversion.convert(input)));
    }

    public static TreeNode convert(int[] input) {
        Queue<TreeNode> q = new LinkedList<>();
        TreeNode root = new TreeNode(input[0]);
        q.offer(root);

        boolean leftIsFull = false;
        for (int i = 1; i < input.length; i++) {
            TreeNode n = input[i] == -1 ? null : new TreeNode(input[i]);
            TreeNode parent = q.peek();

            if (!leftIsFull) {
                parent.left = n;
                leftIsFull = true;
            } else {
                parent.right = n;
                q.remove();
                leftIsFull = false;
            }
            if (n != null) {
                q.offer(n);
            }
        }

        return root;
    }

}
