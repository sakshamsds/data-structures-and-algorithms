/*
    diff = ones - zeros, i
    0   1   1   1   1   1   0   0   0
    -1  0   1   2   3   4   3   2   1
 */

class Solution {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> diffs = new HashMap<>();
        diffs.put(0, -1);
        int zeros = 0;
        int largest = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) zeros++;
            int diff = i + 1 - 2 * zeros;
            // System.out.println(diff);
            if (diffs.containsKey(diff)) {
                largest = Math.max(largest, i - diffs.get(diff));
            } else {
                diffs.put(diff, i);
            }
        }
        return largest;
    }
}