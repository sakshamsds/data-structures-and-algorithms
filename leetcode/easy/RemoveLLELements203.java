package easy;

import ds.ListNode;

// 203. Remove Linked List Elements
// https://leetcode.com/problems/remove-linked-list-elements/

public class RemoveLLELements203 {
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        ListNode node1 = new ListNode(2);
        head.next = node1;
        ListNode node2 = new ListNode(6);
        node1.next = node2;
        ListNode node3 = new ListNode(3);
        node2.next = node3;
        ListNode node4 = new ListNode(4);
        node3.next = node4;
        ListNode node5 = new ListNode(5);
        node4.next = node5;
        ListNode node6 = new ListNode(6);
        node5.next = node6;

        int val = 6;
        ListNode result = removeElements(head, val);

        while (result != null) {
            System.out.println("-> " + result.val);
            result = result.next;
        }
    }

    public static ListNode removeElements(ListNode head, int val) {
        ListNode origin = new ListNode(0);
        ListNode previous = origin;
        origin.next = head;

        while (head != null) {
            if (head.val == val) {
                previous.next = head.next;
            } else {
                previous = previous.next;
            }
            head = head.next;
        }

        return origin.next;
    }

}
