class Solution {
    public int concatenatedBinary(int n) {
        int res = 0;
        int MOD = 1_000_000_007;

        for (int num = 1; num < n + 1; num++) {
            String binary = Integer.toBinaryString(num);
            for (int i = 0; i < binary.length(); i++) {
                res = (res * 2 + (binary.charAt(i) - '0')) % MOD;
            }
        }

        return res;
    }
}