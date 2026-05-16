class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int maxAbility = Arrays.stream(worker).max().getAsInt();
        int[] maxProfit = new int[maxAbility + 1];

        for (int i = 0; i < difficulty.length; i++) {
            if (difficulty[i] <= maxAbility) {
                maxProfit[difficulty[i]] = Math.max(maxProfit[difficulty[i]], profit[i]);
            }
        }

        for (int i = 0; i < maxAbility; i++) {
            maxProfit[i + 1] = Math.max(maxProfit[i], maxProfit[i + 1]);
        }

        int totalProfit = 0;
        for (int ability : worker) {
            totalProfit += maxProfit[ability];
        }

        return totalProfit;
    }
}