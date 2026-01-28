/*
    1   1   1               k=1

    1   -1  -1               k=-2
    0 - 2
    1 - 1
 */

class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> freqs = new HashMap<>();
        freqs.put(0, 1);
        int cur_prefix = 0;
        int num_arr = 0;
        for (int num : nums) {
            cur_prefix += num;
            num_arr += freqs.getOrDefault(cur_prefix - k, 0);
            freqs.put(cur_prefix, freqs.getOrDefault(cur_prefix, 0) + 1);
        }
        return num_arr;
    }
}
