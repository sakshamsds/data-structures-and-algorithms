class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> uniques = new HashSet<>();
        for (int num : nums) {
            uniques.add(num);
        }
        return uniques.size() != nums.length;
    }
}