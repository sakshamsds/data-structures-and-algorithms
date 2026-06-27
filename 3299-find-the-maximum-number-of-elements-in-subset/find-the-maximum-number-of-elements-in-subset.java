class Solution {
    public int maximumLength(int[] nums) {
        Map<Long, Integer> cnt = new HashMap<>();
        for (int num : nums) {
            cnt.merge((long) num, 1, Integer::sum);
        }

        int oneCnt = cnt.getOrDefault(1L, 0);
        int maxLength = oneCnt - 1 + (oneCnt & 1);
        cnt.remove(1L);

        for (long num : cnt.keySet()) {
            int curLength = 0;
            while (cnt.containsKey(num)) {
                if (cnt.get(num) == 1) {
                    curLength += 1;
                    break;
                }
                curLength += 2;
                num *= num;
            }
            maxLength = Math.max(maxLength, curLength - 1 + (curLength & 1));
        }

        return maxLength;
    }
}