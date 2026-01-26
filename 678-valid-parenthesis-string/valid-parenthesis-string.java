class Solution {

    private Boolean[][] memo;

    public boolean checkValidString(String s) {
        int n = s.length();
        memo = new Boolean[n][n];
        return dfs(s, 0, 0);
    }

    private boolean dfs(String s, int i, int left) {
        if (i == s.length()) {
            return left == 0;
        }
        if (left < 0) {
            return false;
        }

        if (memo[i][left] != null) {
            return memo[i][left];
        }

        boolean result = false;
        char c = s.charAt(i);

        if (c == '(') {
            result = dfs(s, i + 1, left + 1);
        } else if (c == ')') {
            result = dfs(s, i + 1, left - 1);
        } else {
            result = dfs(s, i + 1, left + 1) ||
                    dfs(s, i + 1, left) ||
                    dfs(s, i + 1, left - 1);
        }
        return memo[i][left] = result;
    }
}