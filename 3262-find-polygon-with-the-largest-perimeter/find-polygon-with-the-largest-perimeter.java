class Solution {
    public long largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        long perimeter = 0;
        for (int num: nums){
            perimeter += num;
        }
        for (int i = nums.length - 1; i >= 2; i--) {
            if (perimeter > 2 * nums[i]) {
                return perimeter;
            }
            perimeter -= nums[i];
        }
        return -1;
    }
}