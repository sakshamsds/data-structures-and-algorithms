/**
    s1 + c or s2 + c
    dp[i][j] = (c in s1) dp[i - 1][j] or (c in s2) dp[i][j - 1]

            d   b   b   c   a
        1   0   
    a   1   0   
    a   1   1   1   1   1   0
    b   0   1            
    c                       
    c                   

    dp[dbbca][aabc]     add c to s1
    dp[dbbc][aabcc]     add a to s2
 */

class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length()) return false;

        boolean[] dp = new boolean[s2.length() + 1];
        dp[0] = true;
        for (int j = 1; j < dp.length; j++) {
            dp[j] = dp[j - 1] && (s2.charAt(j - 1) == s3.charAt(j - 1));
        }

        for (int i = 0; i < s1.length(); i++) {
            dp[0] = dp[0] && (s1.charAt(i) == s3.charAt(i));
            for (int j = 1; j < dp.length; j++) {
                boolean from_top = dp[j] && (s1.charAt(i) == s3.charAt(i + j));
                boolean from_left = dp[j - 1] && (s2.charAt(j - 1) == s3.charAt(i + j));
                dp[j] = from_top || from_left;
            }
        }
        return dp[dp.length - 1];
    }
}