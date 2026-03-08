class Solution {
    public String findDifferentBinaryString(String[] nums) {
        StringBuilder sb = new StringBuilder();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            sb.append(1 ^ nums[i].charAt(i) - '0');
        }
        return sb.toString();
    }
}