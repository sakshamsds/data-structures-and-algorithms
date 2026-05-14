class Solution {
    public boolean isGood(int[] nums) {
        int n = nums.length - 1;

        int[] freqArray = new int[n + 1];
        for (int num : nums) {
            if (num > n) return false;
            freqArray[num]++;
        }
        freqArray[n]--;

        return Arrays.stream(freqArray, 1, n + 1).allMatch(count -> count == 1);
    }
}