class Solution {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer, Integer> freqs = new HashMap<>();
        int maxFreq = Integer.MIN_VALUE;
        int res = 0;
        for (int num : nums) {
            int f = freqs.getOrDefault(num, 0) + 1;
            freqs.put(num, f);
            if (f > maxFreq) {
                maxFreq = f;
                res = f;
            } else if (f == maxFreq) {
                res += f;
            }
        }
        return res;
    }
}