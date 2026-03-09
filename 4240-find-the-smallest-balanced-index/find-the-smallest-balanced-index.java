class Solution {
    public int smallestBalancedIndex(int[] nums) {
        long leftSum = 0;
        for (int num : nums) {
            leftSum += num;
        }
        long rightPdt = 1;
        // System.out.println(leftSum);

        // only one balanced index
        for (int i = nums.length - 1; i >= 0; i--) {
            leftSum -= nums[i];
            if (leftSum == rightPdt) {
                return i;
            } else if (leftSum < rightPdt) {
                break;
            }
            rightPdt *= nums[i];
        }

        return -1;
    }
}