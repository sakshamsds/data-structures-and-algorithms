package easy;

// https://leetcode.com/problems/merge-two-sorted-lists
// 21. Merge Two Sorted Lists

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

public class MergeSortedLLists21 {
    public static void main(String[] args) {

        ListNode list1 = new ListNode(1);
        ListNode list1Node1 = new ListNode(2);
        ListNode list1Node2 = new ListNode(4);
        list1.next = list1Node1;
        list1Node1.next = list1Node2;

        ListNode list2 = new ListNode(1);
        ListNode list2Node1 = new ListNode(3);
        ListNode list2Node2 = new ListNode(4);
        list2.next = list2Node1;
        list2Node1.next = list2Node2;

        ListNode result = mergeTwoLists(list1, list2);

        while (result != null) {
            System.out.println("-> " + result.val);
            result = result.next;
        }

    }

    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode(0);
        ListNode currentNode = head;

        while (list1 != null && list2 != null) {
            if (list1.val > list2.val) {
                currentNode.next = list2;
                list2 = list2.next;
            } else {
                currentNode.next = list1;
                list1 = list1.next;
            }
            currentNode = currentNode.next;
        }

        if (list1 != null) {
            currentNode.next = list1;
        } else if (list2 != null) {
            currentNode.next = list2;
        }

        return head.next;
    }
}
