/*
    partition at i or not partition at i
    a   a   b
    a   ab
    aa  b
    aab
 */

class Solution {

    private List<List<String>> response = new ArrayList<>();
    private int N;

    public List<List<String>> partition(String s) {
        N = s.length();
        backtrack(0, s, new ArrayList<>());
        return response;
    }

    private boolean isPalindrome(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) {
                return false;
            }
        }
        return true;
    }

    private void backtrack(int start, String s, List<String> substrings) {
        if (start == N) {
            response.add(new ArrayList<>(substrings));
            return;
        }

        for (int end = start; end < s.length(); end++) {
            if (!isPalindrome(s, start, end)) {
                continue;
            }
            substrings.add(s.substring(start, end + 1));
            backtrack(end + 1, s, substrings);
            substrings.remove(substrings.size() - 1);
        }
    }
}