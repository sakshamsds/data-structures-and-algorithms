package leetcode.easy;

import java.util.HashSet;
import java.util.Set;


// https://leetcode.com/problems/contains-duplicate/
// 217. Contains Duplicate

public class ContainsDuplicate {

	public static void main(String[] args) {
		int[] nums = new int[] { 1, 2, 3, 4, 4 };
		System.out.println(containsDuplicate(nums));
	}

	public static boolean containsDuplicate(int[] nums) {
//		// brute force
//		for(int i=0; i<nums.length; i++) {
//			for(int j=i+1; j<nums.length; j++) {
//				if(nums[j]==nums[i])
//					return true;
//			}
//		}
//		return false;

		Set<Integer> values = new HashSet<>();
//		for (int num : nums) {
//			values.add(num);
//		}
//		return values.size() != nums.length;

		for(int num: nums) {
			if(!values.add(num))
				return true;
		}
		return false;

	}
}
