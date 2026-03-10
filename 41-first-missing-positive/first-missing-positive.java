/**
    5
    2   4   5   8   1
            -5
                    -1
    -2

    0   1   2   3
    
    3   4   -1  1
    -3  4   4   -1
 */

class Solution {
    public int firstMissingPositive(int[] nums) {
        // convert neg to big postiive
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= 0) {
                nums[i] = nums.length + 1;
            }
        }

        // System.out.println(Arrays.toString(nums));

        // make index value neg
        for (int num : nums) {
            int idx = Math.abs(num) - 1;
            if (idx >= nums.length) continue;
            nums[idx] = -Math.abs(nums[idx]);
        }

        // System.out.println(Arrays.toString(nums));
        
        // find first positive
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) return i + 1;
        }
        return nums.length + 1;
    }
}