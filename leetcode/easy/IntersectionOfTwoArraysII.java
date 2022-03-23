package easy;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/intersection-of-two-arrays-ii/
// 350. Intersection of Two Arrays II

public class IntersectionOfTwoArraysII {

	public static void main(String[] args) {

		int[] nums1 = new int[] { 4, 9, 5 };
		int[] nums2 = new int[] { 9, 4, 9, 8, 4 };
//		int[] nums1 = new int[] { 1, 2, 2, 1 };
//		int[] nums2 = new int[] { 2, 2 };

		System.out.println(Arrays.toString(intersect(nums1, nums2)));

	}

	public static int[] intersect(int[] nums1, int[] nums2) {
		// Solution 2, O(max(n,m))
		// key = int value, value = frequency
		Map<Integer, Integer> frequencyMap = new HashMap<>();

		for (int i = 0; i < nums1.length; i++) {
			frequencyMap.put(nums1[i], frequencyMap.getOrDefault(nums1[i], 0) + 1);
		}

		int numsCommonEements = 0;
		for (int i = 0; i < nums2.length; i++) {
//			System.out.println(Arrays.toString(nums1));
//			System.out.println(frequencyMap);
			if (frequencyMap.containsKey(nums2[i]) && frequencyMap.get(nums2[i]) > 0) {
				frequencyMap.put(nums2[i], frequencyMap.get(nums2[i]) - 1);
				nums1[numsCommonEements++] = nums2[i];
			}
		}
		return Arrays.copyOfRange(nums1, 0, numsCommonEements);
	}

//	public static int[] intersect(int[] nums1, int[] nums2) {
//		
//		// Solution 1, O(n*m)
//		
//		List<Integer> intersection = new ArrayList<>();
//		
//		for (int i = 0; i < nums1.length; i++) {
//			for (int j = 0; j < nums2.length; j++) {
//				if (nums1[i] == nums2[j]) {
//					intersection.add(nums1[i]);
//					nums2[j] = -1;
//					break;
//				}
//			}
//		}
//		
//		int[] intersectionArray = new int[intersection.size()];
//		for (int i = 0; i < intersectionArray.length; i++) {
//			intersectionArray[i] = intersection.get(i);
//		}
//		
//		return intersectionArray;
//	}

}
