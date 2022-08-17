package medium;

import java.util.Arrays;

// https://www.youtube.com/watch?v=cQ1Oz4ckceM
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// 167. Two Sum II - Input Array Is Sorted

public class TwoSumII167 {
    public static void main(String[] args) {
        int[] numbers = new int[] { 5, 25, 75 };
        int target = 100;
        System.out.println(Arrays.toString(new TwoSumII167().twoSum(numbers, target)));
    }

    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length - 1;

        while (start != end) {
            int sum = numbers[start] + numbers[end];

            if (sum > target) {
                end--;
            } else if (sum < target) {
                start++;
            } else {
                break;
            }
        }

        return new int[]{start+1, end+1};
    }
}
