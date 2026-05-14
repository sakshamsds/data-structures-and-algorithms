class Solution {
    public boolean isGood(int[] nums) {
        // find the max element
        // freq array, all 1 except last one

        int max = 0;
        for (int num : nums) {
            max = Math.max(num, max);
        }

        int[] freqArray = new int[max];
        for (int num : nums) {
            freqArray[num - 1]++;
        }

        freqArray[max - 1]--;
        for (int freq : freqArray) {
            if (freq != 1) return false;
        }        

        return true;
    }
}