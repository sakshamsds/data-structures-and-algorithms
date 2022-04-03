package easy;

// https://leetcode.com/problems/linked-list-cycle/
// 141. Linked List Cycle

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class LinkedListCycle141 {

    public static void main(String[] args) {
        ListNode head = new ListNode(3);
        ListNode node1 = new ListNode(2);
        ListNode node2 = new ListNode(0);
        ListNode node3 = new ListNode(-4);
        head.next = node1;
        node1.next = node2;
        node2.next = node3;
        node3.next = node1;

        System.out.println(hasCycle(head));
    }

    // Floyd's cycle detection algorithm
    public static boolean hasCycle(ListNode head) {
        ListNode slowNode = head;
        ListNode fastNode = head;

        while (fastNode != null && fastNode.next != null) {

            slowNode = slowNode.next;
            fastNode = fastNode.next.next;

            if (slowNode.equals(fastNode)) {
                return true;
            }
        }

        return false;
    }
}
