package easy;

import java.util.Stack;

// https://leetcode.com/problems/valid-parentheses/
// 20. Valid Parentheses

public class ValidParentheses20 {
    public static void main(String[] args) {
        String s = "()[]{}}";
        System.out.println(isValid(s));
    }

    public static boolean isValid(String s) {
        Stack<Character> st = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!st.empty() && isMatching(st.peek(), c)) {
                st.pop();
            } else {
                st.push(c);
            }
        }

        return st.empty();
    }

    public static boolean isMatching(char a, char b) {
        if ((a == '(' && b == ')') || (a == '[' && b == ']') || (a == '{' && b == '}')) {
            return true;
        }
        return false;
    }

}
