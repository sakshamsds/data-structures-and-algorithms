package easy;

import java.util.Stack;

// 104. Maximum Depth of Binary Tree
// https://leetcode.com/problems/maximum-depth-of-binary-tree/

import ds.TreeNode;

public class BTMaxDepth104 {
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

        System.out.println(maxDepth(root));
    }

    // // recursive
    // public static int maxDepth(TreeNode root) {
    // // O(N)
    // if (root == null) {
    // return 0;
    // }
    // return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    // }

    // // iterative BFS
    // public static int maxDepth(TreeNode root) {
    // // O(N)
    // if (root == null) {
    // return 0;
    // }

    // Queue<TreeNode> queue = new LinkedList<>();
    // queue.offer(root);

    // int currDepth = 0;
    // while (!queue.isEmpty()) {
    // // the depth of the level being processed
    // currDepth++;

    // int size = queue.size();
    // for (int i = 0; i < size; i++) {
    // TreeNode node = queue.remove();
    // if (node.left != null) {
    // queue.offer(node.left);
    // }
    // if (node.right != null) {
    // queue.offer(node.right);
    // }
    // }
    // }

    // return currDepth;
    // }

    // itertive DFS, top down, recursive is bottoms up
    public static int maxDepth(TreeNode root) {

        if (root == null) {
            return 0;
        }

        Stack<Pair<TreeNode, Integer>> st = new Stack<>();
        st.push(new Pair<>(root, 1));

        int maxDepth = 0;
        while (!st.empty()) {
            Pair<TreeNode, Integer> pair = st.pop();
            TreeNode node = pair.key;
            int currDepth = pair.value;

            maxDepth = Math.max(maxDepth, currDepth);
            if (node.left != null) {
                st.push(new Pair<>(node.left, currDepth + 1));
            }
            if (node.right != null) {
                st.push(new Pair<>(node.right, currDepth + 1));
            }
        }

        return maxDepth;
    }

}

class Pair<K, V> {
    K key;
    V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }
}
