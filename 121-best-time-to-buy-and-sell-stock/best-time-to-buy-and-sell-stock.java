class Solution {
    public int maxProfit(int[] prices) {
        int min_price = Integer.MAX_VALUE;
        int max_profit = 0;
        for (int price : prices) {
            max_profit = Math.max(max_profit, price - min_price);
            min_price = Math.min(min_price, price);
        }
        return max_profit;
    }
}