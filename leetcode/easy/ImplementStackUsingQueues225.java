package easy;

import java.util.LinkedList;
import java.util.Queue;

// https://leetcode.com/problems/implement-stack-using-queues/
// 225. Implement Stack using Queues

public class ImplementStackUsingQueues225 {
    public static void main(String[] args) {

    }
}

class MyStack {

    Queue<Integer> q;

    public MyStack() {
        q = new LinkedList<>();
    }

    public void push(int x) {
        q.offer(x);

        int size = q.size() - 1;
        // number of elements to push to the back

        while (size-- > 0) {
            q.offer(q.poll());
        }
    }

    public int pop() {
        // Removes the element on the top of the stack and returns it.
        return q.poll();
    }

    public int top() {
        // Returns the element on the top of the stack.
        return q.peek();
    }

    public boolean empty() {
        return q.isEmpty();
    }
}