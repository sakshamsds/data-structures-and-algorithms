package easy;

// https://leetcode.com/problems/remove-duplicates-from-sorted-list/
// 83. Remove Duplicates from Sorted List

public class RemoveDuplicatesFromSortedLL83 {
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        ListNode node1 = new ListNode(2);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(2);
        head.next = node1;
        node1.next = node2;
        node2.next = node3;
        node3.next = null;

        ListNode result = deleteDuplicates(head);
        while (result != null) {
            System.out.println("-> " + result.val);
            result = result.next;
        }
    }

    public static ListNode deleteDuplicates(ListNode head) {

        // // two pointers approach
        // ListNode start = head;
        // ListNode prev = start;

        // while (head != null) {
        // // System.out.println("head: " + head.val);
        // if (head.val == prev.val) {
        // prev.next = head.next;
        // } else {
        // prev = prev.next;
        // }
        // head = head.next;
        // }

        // one pointer approach
        ListNode currentNode = head;

        while (currentNode != null && currentNode.next != null) {
            if (currentNode.val == currentNode.next.val) {
                currentNode.next = currentNode.next.next;
            } else {
                currentNode = currentNode.next;
            }
        }

        return head;
    }

}
