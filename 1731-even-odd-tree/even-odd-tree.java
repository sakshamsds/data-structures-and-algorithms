/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isEvenOddTree(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int level = 0;
        while (!q.isEmpty()) {
            int level_size = q.size();
            boolean is_odd_level = level % 2 == 1;
            int prev = -1;
            if (is_odd_level) {
                prev = Integer.MAX_VALUE;
            } else {
                prev = 0;
            }
            for (int i = 0; i < level_size; i++) {
                TreeNode cur = q.poll();
                if (is_odd_level) {
                    if (cur.val % 2 == 1 || prev <= cur.val) {
                        return false;
                    }
                } else {
                    if (cur.val % 2 == 0 || prev >= cur.val) {
                        return false;
                    }
                }
                if (cur.left != null) {
                    q.add(cur.left);
                }
                if (cur.right != null) {
                    q.add(cur.right);
                }
                prev = cur.val;
            }
            level++;
        }
        return true;
    }
}