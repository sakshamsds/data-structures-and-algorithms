class Solution {
    public int rob(int[] nums) {
        return Math.max(nums[0], 
                        Math.max(helper(nums, 0, nums.length - 1), 
                                 helper(nums, 1, nums.length)));
    }

    private static int helper(int[] nums, int startIdx, int endIdx) {
        int rob = 0;
        int noRob = 0;
        for (int i = startIdx; i < endIdx; i++) {
            int temp = rob;
            rob = noRob + nums[i];
            noRob = Math.max(temp, noRob);
        }
        return Math.max(rob, noRob);
    }
}