class Solution {
    public int rob(int[] nums) {
        int rob = 0;
        int noRob = 0;

        for (int num : nums) {
            int temp = rob;
            rob = noRob + num;
            noRob = Math.max(temp, noRob);
        }

        return Math.max(rob, noRob);
    }
}