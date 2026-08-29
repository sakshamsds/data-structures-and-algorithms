class Solution {
    public int missingMultiple(int[] nums, int k) {
        Set<Integer> available = new HashSet<>();
        for (int num : nums) {
            available.add(num);
        }
        int multiple = k;
        while (available.contains(multiple)) {
            multiple += k;
        }
        return multiple;
    }
}