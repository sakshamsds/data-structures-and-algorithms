class Solution {
    public int minOperations(String s) {
        // zeros at odd, ones at even position
        // score = total - zeros_odd - ones_even
        // score = total - ones_odd - zeros_even

        int zeros_odd = 0, zeros_even = 0, ones_odd = 0, ones_even = 0;
        for (int i = 0; i < s.length(); i++) {
            int digit = s.charAt(i) - '0';
            if ((i & 1) == 1) {
                zeros_odd += 1 ^ digit;
                ones_odd += digit;
            } else {
                zeros_even += 1 ^ digit;
                ones_even += digit;
            }
        }

        return s.length() - Math.max(zeros_odd + ones_even, zeros_even + ones_odd);
    }
}