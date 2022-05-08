package medium;

import java.util.Arrays;

// https://leetcode.com/problems/rotate-array/
// 189. Rotate Array

public class RotateArray189 {
    public static void main(String[] args) {
        int[] nums = new int[] { 1, 2, 3, 4, 5, 6, 7 };
        int k = 3;
        new RotateArray189().rotate(nums, k);
        System.out.println(Arrays.toString(nums));
    }

    // not using extra space
    public void rotate(int[] nums, int k) {
        int rotations = k % nums.length;

        reverseAnArray(nums, 0, nums.length - rotations - 1);
        // System.out.println(Arrays.toString(nums));
        reverseAnArray(nums, nums.length - rotations, nums.length - 1);
        // System.out.println(Arrays.toString(nums));
        reverseAnArray(nums, 0, nums.length - 1);
        // System.out.println(Arrays.toString(nums));
    }

    public void reverseAnArray(int[] nums, int start, int end) {
        int left = start;
        int right = end;
        while (left < right) {
            nums[left] = nums[right] - nums[left] + (nums[right] = nums[left]);
            left++;
            right--;
        }
    }

    // // using extra space
    // public void rotate(int[] nums, int k) {
    // int rotations = k % nums.length;
    // int[] temp = new int[nums.length];

    // for (int i = 0; i < rotations; i++) {
    // temp[i] = nums[nums.length - rotations + i];
    // }

    // for (int i = rotations; i < nums.length; i++) {
    // temp[i] = nums[i - rotations];
    // }

    // // System.out.println(Arrays.toString(temp));

    // for (int i = 0; i < nums.length; i++) {
    // nums[i] = temp[i];
    // }
    // }
}
