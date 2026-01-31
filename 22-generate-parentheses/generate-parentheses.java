/*
    (   (   (
            )
        )   (
            )
 */

class Solution {

    private List<String> valid = new ArrayList<>();
    private Integer total_length;

    public List<String> generateParenthesis(int n) {
        total_length = 2 * n;
        backtrack(0, "");
        return valid;        
    }

    private void backtrack(int idx, String s) {
        if (idx == total_length) {
            // System.out.println(idx + "," + total_length + "," + s);
            if (isValid(s)) {
                valid.add(s);
            }
            return;
        }
        backtrack(idx + 1, s + '(');
        backtrack(idx + 1, s + ')');
    }

    private boolean isValid(String s) {
        if (s.length() < 2) {
            return false;
        }
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else {        // closing parentheses
                if (stack.isEmpty() || stack.peek() != '(') {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}