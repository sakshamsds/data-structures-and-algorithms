class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] res = new int[nums.length];
        int even_i = 0;
        int odd_i = 1;
        for (int num : nums) {
            if (num > 0) {
                res[even_i] = num;
                even_i += 2;
            } else {
                res[odd_i] = num;
                odd_i += 2;
            } 
        }
        return res;
    }
}