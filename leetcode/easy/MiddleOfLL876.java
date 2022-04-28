package easy;

import ds.ListNode;

// 876. Middle of the Linked List
// https://leetcode.com/problems/middle-of-the-linked-list/

public class MiddleOfLL876 {
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        ListNode node1 = new ListNode(0);
        ListNode node2 = new ListNode(1);
        head.next = node1;
        node1.next = node2;

        System.out.println(new MiddleOfLL876().middleNode(head).val);
    }

    public ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while(fast!=null && fast.next!=null){
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }

    // public ListNode middleNode(ListNode head) {
    //     Map<Integer, ListNode> positionMap = new HashMap<>();

    //     int position = 0;
    //     while (head != null) {
    //         positionMap.put(position++, head);
    //         head = head.next;
    //     }
    //     System.out.println(position);

    //     return positionMap.get(position / 2);
    // }

}
