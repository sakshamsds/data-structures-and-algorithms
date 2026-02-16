class Solution {
    public int reverseBits(int n) {
        int power = 31, res = 0;
        while (n > 0) {
            res += (n & 1) << power;
            n = n >> 1;
            power--;
        }
        return res;
    }
}