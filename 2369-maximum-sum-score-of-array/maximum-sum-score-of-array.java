class Solution {
    public long maximumSumScore(int[] nums) {
        long prefix = 0;
        long suffix = 0;
        for (int num : nums) {
            suffix += num;
        }

        long max_sum_score = nums[0];
        for (int num : nums) {
            prefix += num;
            max_sum_score = Math.max(max_sum_score, Math.max(prefix, suffix));
            suffix -= num;
        }

        return max_sum_score;
    }
}