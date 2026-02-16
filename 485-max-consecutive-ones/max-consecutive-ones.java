class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxOnes = 0, curOnes = 0;
        for (int num : nums) {
            if (num == 0) {
                curOnes = 0;
            } else {
                curOnes += 1;
                maxOnes = Math.max(maxOnes, curOnes);
            }
        }
        return maxOnes;
    }
}