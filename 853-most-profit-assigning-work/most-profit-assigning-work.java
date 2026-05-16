class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        // sort (difficulty, profit)
        List<int[]> jobProfile = new ArrayList<>();
        for (int i = 0; i < difficulty.length; i++) {
            jobProfile.add(new int[] {difficulty[i], profit[i]});
        }
        Collections.sort(jobProfile, (a, b) -> Integer.compare(a[0], b[0]));
        Arrays.sort(worker);

        int totalProfit = 0;
        int ptr = 0;
        int maxProfit = 0;

        for (int ability : worker) {
            while (ptr < jobProfile.size() && ability >= jobProfile.get(ptr)[0]) {
                maxProfit = Math.max(maxProfit, jobProfile.get(ptr)[1]);
                ptr++;
            }
            totalProfit += maxProfit;
        }
        return totalProfit;
    }
}