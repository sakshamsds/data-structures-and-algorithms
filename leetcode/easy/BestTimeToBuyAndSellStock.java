package easy;

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// 121. Best Time to Buy and Sell Stock

public class BestTimeToBuyAndSellStock {

	public static void main(String[] args) {

		int[] prices = new int[] { 7, 6, 4, 3, 1 };
//		int[] prices = new int[] { 7, 1, 5, 3, 6, 4 };
		// 5712
		System.out.println(maxProfit(prices));

	}

	public static int maxProfit(int[] prices) {

		// Solution 2, O(n)

		int maxProfit = 0;
		int leastSoFar = prices[0];
		int profitIfSoldToday = 0;

		for (int i = 0; i < prices.length; i++) {
			leastSoFar = Math.min(leastSoFar, prices[i]);
			profitIfSoldToday = prices[i] - leastSoFar;
			maxProfit = Math.max(maxProfit, profitIfSoldToday);
		}

		return maxProfit;
	}

//		public static int maxProfit(int[] prices) {
//		
//		// Solution 1: brute force, TLE
//		
//		int maxProfit = 0;
//		
//		for (int i = 0; i < prices.length; i++) {
//			
//			int buy = prices[i];
//			for (int j = i + 1; j < prices.length; j++) {
//				int sell = prices[j];
//				
//				if (sell > buy) {
//					maxProfit = Math.max(maxProfit, sell - buy);
//				}
//				
//			}
//		}
//		
//		return maxProfit;
//	}
}
