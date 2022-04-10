package easy;

// https://leetcode.com/problems/reverse-linked-list/
// 206. Reverse Linked List

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

public class ReverseLinkedList206 {
    public static void main(String[] args) {
        ListNode head = new ListNode(3);
        ListNode node1 = new ListNode(2);
        ListNode node2 = new ListNode(0);
        ListNode node3 = new ListNode(-4);
        head.next = node1;
        node1.next = node2;
        node2.next = node3;
        node3.next = null;

        ListNode result = reverseList(head);
        while (result != null) {
            System.out.println("-> " + result.val);
            result = result.next;
        }
    }

    public static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode temp;

        while (head != null) {
            temp = head;
            head = head.next;
            temp.next = prev;
            prev = temp;
        }

        return prev;
    }
}
