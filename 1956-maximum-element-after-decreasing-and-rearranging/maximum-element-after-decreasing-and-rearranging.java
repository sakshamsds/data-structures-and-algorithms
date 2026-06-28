class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        int n = arr.length;
        int[] freqs = new int[n + 1];

        for (int num : arr) {
            freqs[Math.min(num, n)]++;
        }

        int maxElement = 0;
        for (int i = 1; i < n + 1; i++) {
            maxElement = Math.min(maxElement + freqs[i], i);
        }
        return maxElement;
    }
}