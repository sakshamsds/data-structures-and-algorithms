/*
    7   8   29  1   0   12  5
    greedy

    if prev <= cur, get profit
    else buy
 */

class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) {
            return 0;
        }

        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i - 1] <= prices[i]) {
                profit += prices[i] - prices[i - 1];
            }
        }
        return profit;
    }
}