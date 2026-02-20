class Solution {
    private Map<String, Boolean> dp ;
    private String s1;
    private String s2;
    private String s3;

    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length()) return false;
        this.s1 = s1;
        this.s2 = s2;
        this.s3 = s3;
        dp = new HashMap<>();
        return dfs(0, 0, 0);
    }

    private boolean dfs(int i, int j, int k) {
        if (k == s3.length()) return true;

        String state = i + "," + j;
        if (dp.containsKey(state)) {
            return dp.get(state);
        }

        if (i == s1.length()) return s2.substring(j).equals(s3.substring(k));
        if (j == s2.length()) return s1.substring(i).equals(s3.substring(k));

        boolean valid = false;
        if (s1.charAt(i) == s3.charAt(k) && dfs(i + 1, j, k + 1)) valid = true;
        if (s2.charAt(j) == s3.charAt(k) && dfs(i, j + 1, k + 1)) valid = true;

        dp.put(state, valid);
        return valid;
    }
}