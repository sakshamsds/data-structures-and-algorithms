package easy;

import java.util.Stack;

// https://leetcode.com/problems/implement-queue-using-stacks/
// 232. Implement Queue using Stacks

public class ImplementQueueUsingStack232 {
    public static void main(String[] args) {

        MyQueue obj = new MyQueue();
        obj.push(1);
        obj.push(2);
        obj.push(3);
        int param_2 = obj.pop();
        int param_3 = obj.peek();
        boolean param_4 = obj.empty();

        System.out.println(param_2);
        System.out.println(param_3);
        System.out.println(param_4);
    }

}

class MyQueue {

    private Stack<Integer> input = new Stack<>();

    // st2 will be our queue for FIFO implementation
    private Stack<Integer> output = new Stack<>();

    public MyQueue() {
    }

    public void push(int x) {
        input.push(x);
    }

    public int pop() {
        peek();
        return output.pop();
    }

    public int peek() {
        if(output.empty()){
            while(!input.empty()){
                output.push(input.pop());
            }
        }
        return output.peek();
    }

    public boolean empty() {
        return input.isEmpty() && output.empty();
    }
}
