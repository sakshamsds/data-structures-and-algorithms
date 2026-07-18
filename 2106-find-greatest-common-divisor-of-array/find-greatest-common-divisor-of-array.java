class Solution {
    public int findGCD(int[] nums) {
        int max = 0;
        int min = 1001;

        for (int num : nums) {
            if (num > max) max = num;
            if (num < min) min = num;
        }

        return gcd(min, max);
    }

    private int gcd(int a, int b) {
        if (b % a == 0) return a;
        return gcd(b % a, a);
    }
}