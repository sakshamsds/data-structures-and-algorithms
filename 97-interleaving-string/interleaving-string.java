class Solution {
    private Map<String, Boolean> dp ;
    private String s1;
    private String s2;
    private String s3;

    public boolean isInterleave(String s1, String s2, String s3) {
        this.s1 = s1;
        this.s2 = s2;
        this.s3 = s3;
        dp = new HashMap<>();
        if (s1.length() + s2.length() != s3.length()) return false;
        return dfs(0, 0, 0);
    }

    private boolean dfs(int i, int j, int k) {
        if (k == s3.length()) return true;

        String state = i + "," + j + "," + k;
        if (dp.containsKey(state)) {
            return dp.get(state);
        }

        boolean valid = false;
        if (i < s1.length() && s1.charAt(i) == s3.charAt(k) && dfs(i + 1, j, k + 1)) valid = true;
        if (j < s2.length() && s2.charAt(j) == s3.charAt(k) && dfs(i, j + 1, k + 1)) valid = true;

        dp.put(state, valid);
        return valid;
    }
}