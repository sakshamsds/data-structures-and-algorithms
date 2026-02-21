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

        int[] dp = new int[s2.length() + 1];
        Arrays.fill(dp, 0);
        dp[0] = 1;
        for (int j = 1; j < dp.length; j++) {
            if (s2.charAt(j - 1) == s3.charAt(j - 1)) {
                dp[j] = 1;
            } else {
                break;
            }
        }

        boolean s1_matching = true;
        for (int i = 0; i < s1.length(); i++) {
            if (s1_matching && s1.charAt(i) == s3.charAt(i)) {
                dp[0] = 1;
            } else {
                dp[0] = 0;
                s1_matching = false;
            }
            for (int j = 1; j < dp.length; j++) {
                if (dp[j] == 1 && s1.charAt(i) == s3.charAt(i + j)) {
                    dp[j] = 1;
                } else if (dp[j - 1] == 1 && s2.charAt(j - 1) == s3.charAt(i + j)) {
                    dp[j] = 1;
                } else {
                    dp[j] = 0;
                }
            }
        }
        return dp[dp.length - 1] == 1;
    }
}