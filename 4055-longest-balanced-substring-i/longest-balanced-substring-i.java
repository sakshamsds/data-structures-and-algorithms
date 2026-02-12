class Solution {

    private int[] freqs;

    private int isBalanced(int valid, int l, int r) {
        for (int freq : freqs) {
            if (freq > 0 && freq != valid) {
                return 0;
            }
        }
        return r - l + 1;
    }

    public int longestBalanced(String s) {
        int balanced = 0;
        for (int i = 0; i < s.length(); i++) {
            freqs = new int[26];
            for (int j = i; j < s.length(); j++) {
                int idx = s.charAt(j) - 'a';
                freqs[idx]++;
                balanced = Math.max(balanced, isBalanced(freqs[idx], i, j));
            }
        }
        return balanced;
    }
}