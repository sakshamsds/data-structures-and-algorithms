class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        // sort (difficulty, profit)
        List<int[]> jobProfile = new ArrayList<>();
        jobProfile.add(new int[] {0, 0});
        for (int i = 0; i < difficulty.length; i++) {
            jobProfile.add(new int[] {difficulty[i], profit[i]});
        }
        Collections.sort(jobProfile, (a, b) -> Integer.compare(a[0], b[0]));

        for (int i = 1; i < jobProfile.size(); i++) {
            jobProfile.get(i)[1] = Math.max(jobProfile.get(i - 1)[1], jobProfile.get(i)[1]);
        }

        int totalProfit = 0;
        for (int ability : worker) {
            int left = 0, right = jobProfile.size();
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (ability < jobProfile.get(mid)[0]) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            totalProfit += jobProfile.get(left - 1)[1];
        }
        return totalProfit;
    }
}