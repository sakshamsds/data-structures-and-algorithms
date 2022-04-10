package easy;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import ds.TreeNode;

// https://leetcode.com/problems/binary-tree-postorder-traversal/
// 145. Binary Tree Postorder Traversal
// *** https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45621/Preorder-Inorder-and-Postorder-Traversal-Iterative-Java-Solution

public class BTPostOrderTraversal145 {

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

        System.out.println(postorderTraversal(root));
    }

    // postorder, left, right, root
    // iterative
    public static List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> output = new ArrayList<>();
        if (root == null)
            return output;

        Stack<TreeNode> st = new Stack<>();
        st.push(root);
        while (!st.empty()) {
            TreeNode visiting = st.pop();
            output.add(0, visiting.val);
            if (visiting.left != null) {
                st.push(visiting.left);
            }
            if (visiting.right != null) {
                st.push(visiting.right);
            }
        }

        return output;
    }

}
