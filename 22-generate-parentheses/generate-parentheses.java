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
        backtrack(new StringBuilder());
        return valid;        
    }

    private void backtrack(StringBuilder sb) {
        if (sb.length() == total_length) {
            // System.out.println(idx + "," + total_length + "," + s);
            if (isValid(sb.toString())) {
                valid.add(sb.toString());
            }
            return;
        }
        sb.append('(');
        backtrack(sb);
        sb.deleteCharAt(sb.length() - 1);
        sb.append(')');
        backtrack(sb);
        sb.deleteCharAt(sb.length() - 1);
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