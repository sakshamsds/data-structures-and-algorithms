package easy;

import ds.ListNode;

// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
// 1290. Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/discuss/1615747/JAVA-or-4-solutions-or-Bit-Manipulation-or-Detailed-Explanation

public class BinaryToInteger1290 {
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        ListNode node1 = new ListNode(0);
        ListNode node2 = new ListNode(1);
        head.next = node1;
        node1.next = node2;

        System.out.println(new BinaryToInteger1290().getDecimalValue(head));
    }

    public int getDecimalValue(ListNode head) {
        int sum = 0;
        while (head != null) {
            sum = 2 * sum + head.val;
            head = head.next;
        }
        return sum;
    }

    // public int getDecimalValue(ListNode head) {
    // List<Integer> list = new LinkedList<>();

    // while (head != null) {
    // list.add(0, head.val);
    // head = head.next;
    // }

    // int sum = 0;
    // for (int i = 0; i < list.size(); i++) {
    // sum += list.get(i) * Math.pow(2, i);
    // }

    // return sum;
    // }

}
