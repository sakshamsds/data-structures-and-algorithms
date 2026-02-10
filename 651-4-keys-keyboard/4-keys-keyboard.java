/*
    1   2   3   4   5   6   7
    1   2   3   4

    dp[j] = max(dp[j - 1] + 1, dp[j - 3] * (num_rep)]
 */

class Solution {
    public int maxA(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 0;
                
        for (int r = 1; r < n + 1; r++) {
            dp[r] = dp[r - 1] + 1;
            for (int l = 1; l < r - 2; l++) {
                dp[r] = Math.max(dp[r], dp[l] * (r - l - 1));
            }
        }
        // System.out.println(Arrays.toString(dp));
        return dp[n];
    }
}