class Solution {
    public int majorityElement(int[] nums) {
        int maj = 0;
        int freq = 0;
        
        for (int num: nums) {
            if (freq == 0) {
                maj = num;
            }
            if (maj == num) {
                freq++;
            } else {
                freq--;
            }
        }
        return maj;
    }
}