class Solution {
    public int minRemoval(int[] nums, int k) {
        Arrays.sort(nums);
        int left = 0;
        for (int num : nums) {
            if (1L * nums[left] * k < num) {
                left++;
            }
        }
        return left;
    }
}