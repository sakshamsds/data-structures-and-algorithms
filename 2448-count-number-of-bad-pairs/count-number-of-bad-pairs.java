import java.util.HashMap;
import java.util.Map;

class Solution {
    public long countBadPairs(int[] nums){
        int n = nums.length;
        long totalPairs = (long) n * (n - 1) / 2;

        Map<Integer, Integer> diffs = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int diff = nums[i] - i;
            diffs.put(diff, diffs.getOrDefault(diff, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : diffs.entrySet()) {
            int v = entry.getValue();
            totalPairs -= (long) v * (v - 1) / 2;
        }
        return totalPairs;
    }
}