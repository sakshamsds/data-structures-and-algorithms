package easy;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/two-sum/
// 1. Two Sum

public class TwoSum {

	public static void main(String[] args) {
		int[] nums = new int[] { 2, 7, 11, 15 };
		int target = 9;
		twoSum(nums, target);
	}

	public static int[] twoSum(int[] nums, int target) {
//		// brute force O(n^2)
//		for (int i = 0; i < nums.length; i++) {
//			for (int j = i + 1; j < nums.length; j++) {
//				if (nums[i] + nums[j] == target) {
//					System.out.println(i + " " + j);
//					return new int[] { i, j };
//				}
//			}
//		}
		
		// use hashmap to store data, O(n)
		// key = subtraction result, value = index
		Map<Integer, Integer> storageMap = new HashMap<>();
		for(int i=0; i<nums.length; i++) {
			if(!storageMap.containsKey(nums[i])) {
				storageMap.put(target - nums[i], i);
			} else {
				System.out.println(storageMap.get(nums[i])+ " " + i);
				return new int[] {storageMap.get(nums[i]), i};
			}
		}
		return null;
	}

}
