package easy;

import java.util.Arrays;

// https://leetcode.com/problems/merge-sorted-array/
// 88. Merge Sorted Array

public class MergeSortedArray88 {
	public static void main(String[] args) {

		int[] nums1 = new int[] { 0 };
		int[] nums2 = new int[] { 1 };
		int m = 0;
		int n = 1;
//		int[] nums1 = new int[] { 1, 2, 3, 0, 0, 0 };
//		int[] nums2 = new int[] { 2, 5, 6 };
//		int m = 3;
//		int n = 3;
		merge(nums1, m, nums2, n);
	}

	public static void merge(int[] nums1, int m, int[] nums2, int n) {

		// solution 2, start from the end, O(m+n), inplace
		int i = m - 1;
		int j = n - 1;

		for (int k = m + n - 1; k >= 0; k--) {

			if (i == -1) {
				nums1[k] = nums2[j];
				j--;
				continue;
			}

			if (j == -1) {
				nums1[k] = nums1[i];
				i--;
				continue;
			}

			if (nums1[i] > nums2[j]) {
				nums1[k] = nums1[i];
				i--;
			} else {
				nums1[k] = nums2[j];
				j--;
			}

		}

		System.out.println(Arrays.toString(nums1));

	}

//	public static void merge(int[] nums1, int m, int[] nums2, int n) {
//
//		// solution 1 make new array, add integers 1 by 1, O(n)
//		int[] nums3 = new int[m + n];
//
//		int nums1Index = 0;
//		int nums2Index = 0;
//
//		for (int i = 0; i < nums3.length; i++) {
//			if (nums1Index == m) {
//				nums3[i] = nums2[nums2Index];
//				nums2Index++;
//				continue;
//			}
//			if (nums2Index == n) {
//				nums3[i] = nums1[nums1Index];
//				nums1Index++;
//				continue;
//			}
//			if (nums1[nums1Index] >= nums2[nums2Index]) {
//				nums3[i] = nums2[nums2Index];
//				nums2Index++;
//			} else {
//				nums3[i] = nums1[nums1Index];
//				nums1Index++;
//			}
//		}
//
//		System.out.println(Arrays.toString(nums3));
//
//		for (int i = 0; i < nums1.length; i++) {
//			nums1[i] = nums3[i];
//		}
//	}

}
