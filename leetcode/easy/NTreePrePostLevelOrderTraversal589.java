package easy;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

import ds.Node;

// 589. N-ary Tree Preorder Traversal
// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

public class NTreePrePostLevelOrderTraversal589 {
    public static void main(String[] args) {
        List<Node> row2 = new ArrayList<>();
        Node node5 = new Node(5);
        Node node6 = new Node(6);
        row2.add(node5);
        row2.add(node6);

        List<Node> row1 = new ArrayList<>();
        Node node3 = new Node(3, row2);
        Node node2 = new Node(2);
        Node node4 = new Node(4);
        row1.add(node3);
        row1.add(node2);
        row1.add(node4);
        Node root = new Node(1, row1);

        // System.out.println(preorder(root).toString());
        // System.out.println(postorder(root).toString());
        System.out.println(levelOrder(root).toString());
    }

    public static List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> output = new ArrayList<>();
        if (root == null) {
            return output;
        }
        Queue<Node> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int levelSize = q.size();

            for (int i = 0; i < levelSize; i++) {
                root = q.poll();
                level.add(root.val);

                if (root.children != null) {
                    for (Node child : root.children) {
                        q.offer(child);
                    }
                }
            }
            output.add(level);
        }
        return output;
    }

    // iterative
    public static List<Integer> preorder(Node root) {
        List<Integer> output = new ArrayList<>();
        if (root == null) {
            return output;
        }

        Stack<Node> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            root = stack.pop();
            output.add(root.val);
            if (root.children != null) {
                int size = root.children.size();
                for (int i = 0; i < size; i++) {
                    stack.push(root.children.get(size - i - 1));
                }
            }
        }

        return output;
    }

    // // root, left, right
    // public static List<Integer> preorder(Node root) {
    // List<Integer> output = new ArrayList<>();
    // preorderHelper(root, output);
    // return output;
    // }

    // public static void preorderHelper(Node root, List<Integer> output) {
    // if (root == null) {
    // return;
    // }

    // output.add(root.val);
    // if (root.children != null) {
    // List<Node> children = root.children;
    // for (Node child : children) {
    // preorderHelper(child, output);
    // }
    // }
    // }

    public static List<Integer> postorder(Node root) {

        List<Integer> output = new ArrayList<>();
        postOrderHelper(root, output);
        return output;
    }

    public static void postOrderHelper(Node root, List<Integer> output) {
        if (root == null) {
            return;
        }
        if (root.children != null) {
            List<Node> children = root.children;
            for (Node child : children) {
                postOrderHelper(child, output);
            }
        }
        output.add(root.val);
    }
}
