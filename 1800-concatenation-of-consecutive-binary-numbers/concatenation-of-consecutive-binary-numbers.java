class Solution {
    public int concatenatedBinary(int n) {
        long res = 0;
        int MOD = 1_000_000_007;
        int shift = 0;

        for (int num = 1; num <= n; num++) {
            if ((num & (num - 1)) == 0) shift++;                
            res = ((res << shift) | num) % MOD;
        }

        return (int) res;
    }
}