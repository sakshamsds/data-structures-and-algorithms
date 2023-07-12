package easy;

// https://leetcode.com/problems/maximum-subarray/
// 53. Maximum Subarray

public class MaximumSubarray {

	public static void main(String[] args) {

		int[] nums = new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
//		int[] nums = new int[] { 5, 4, -1, 7, 8};
//		int[] nums = new int[] { -2};
//		int[] nums = new int[] { -2, 1 };

//		// 1. brute force, calculate all sums
//		int max = nums[0];
//		for (int startIdx = 0; startIdx < nums.length; startIdx++) {
//			int sum = 0;
//
//			for (int i = startIdx; i < nums.length; i++) {
//				sum+=nums[i];
//				max = Math.max(max, sum);
//			}
//		}
//		System.out.println(max);

		// 2. Kadane's Algorithm
		// calculate max subarray sum ending at n'th index
		// https://www.youtube.com/watch?v=86CQq3pKSUw
		int maxGlobal = nums[0];
		int maxCurrent = nums[0];
		//System.out.println("Iteration: " + 0 + "\tCurrent Max: " + maxCurrent + "\tGlobal Max: " + maxGlobal);

		for (int idx = 1; idx < nums.length; idx++) {
			maxCurrent = Math.max(nums[idx], maxCurrent + nums[idx]);
			maxGlobal = Math.max(maxCurrent, maxGlobal);
			//System.out.println("Iteration: " + idx + "\tCurrent Max: " + maxCurrent + "\tGlobal Max: " + maxGlobal);
		}
		System.out.println(maxGlobal);

	}

}
