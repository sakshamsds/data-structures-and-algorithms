class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        Map<Integer, Integer> prefixes = new HashMap<>();  // diff -> idx mapping
        prefixes.put(0, -1);
        int prefix = 0;
        int max_size = 0;
        for (int i = 0; i < nums.length; i++) {
            prefix += nums[i];
            int diff = prefix - k;
            max_size = Math.max(max_size, i - prefixes.getOrDefault(diff, i));
            prefixes.put(prefix, prefixes.getOrDefault(prefix, i));
        }
        return max_size;
    }
}