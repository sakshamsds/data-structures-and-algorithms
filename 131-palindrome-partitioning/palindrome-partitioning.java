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

    private boolean isPalindrome(String substring) {
        for (int i = 0; i < substring.length() / 2; i++) {
            if (substring.charAt(i) != substring.charAt(substring.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }

    private void backtrack(int idx, String s, List<String> substrings) {
        if (idx == N) {
            response.add(new ArrayList<>(substrings));
            return;
        }

        StringBuilder sb = new StringBuilder();
        for (int j = idx; j < s.length(); j++) {
            sb.append(s.charAt(j));
            if (!isPalindrome(sb.toString())) {
                continue;
            }
            substrings.add(sb.toString());
            backtrack(j + 1, s, substrings);
            substrings.remove(substrings.size() - 1);
        }
    }
}