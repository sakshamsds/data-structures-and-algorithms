class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int totalProfit = 0;
        for (int ability : worker) {
            int maxProfit = 0;
            for (int i = 0; i < difficulty.length; i++) {
                if (difficulty[i] <= ability) {
                    maxProfit = Math.max(maxProfit, profit[i]);
                }
            }
            totalProfit += maxProfit;
        }
        return totalProfit;
    }
}