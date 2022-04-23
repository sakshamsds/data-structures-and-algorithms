package easy;

import java.util.Arrays;

// https://leetcode.com/problems/move-zeroes/
// 283. Move Zeroes

public class MoveZeros283 {
    public static void main(String[] args) {
        // int[] nums = new int[] { 0, 1, 0, 3, 12 };
        int[] nums = new int[] { 0, 0, 1 };
        // int[] nums = new int[] { 1, 0, 1 };
        moveZeroes(nums);
    }

    public static void moveZeroes(int[] nums) {
        // O(N)
        int startIdx = 0;
        int endIdx = 1;
        while (endIdx < nums.length) {
            // System.out.println(Arrays.toString(nums));

            if (nums[startIdx] == 0 && nums[endIdx] != 0) {
                nums[startIdx] = nums[endIdx];
                nums[endIdx] = 0;
                startIdx++;
            }
            if (nums[startIdx] != 0) {
                startIdx++;
            }
            endIdx++;
        }
        System.out.println(Arrays.toString(nums));
    }

    // public static void moveZeroes(int[] nums) {
    // // brute force
    // // O(N^2)
    // for (int i = 0; i < nums.length; i++) {
    // if (nums[i] == 0) {
    // // shift this to end by swapping
    // int indexOfZero = i;
    // for (int j = i; j < nums.length - 1; j++) {
    // // System.out.println(Arrays.toString(nums));
    // if (nums[j + 1] == 0) {
    // continue;
    // }

    // nums[indexOfZero] = nums[j + 1];
    // nums[j + 1] = 0;
    // indexOfZero = j + 1;
    // }
    // }
    // }
    // // System.out.println(Arrays.toString(nums));
    // }
}
