package easy;

import java.util.Arrays;

// 977. Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/
// https://leetcode.com/problems/squares-of-a-sorted-array/discuss/221922/Java-two-pointers-O(N)

public class SquaresOfSortedArray977 {
    public static void main(String[] args) {
        System.out
                .println(Arrays.toString(new SquaresOfSortedArray977().sortedSquares(new int[] { -4, -1, 0, 3, 10 })));
    }

    public int[] sortedSquares(int[] nums) {
        // merge together
        int output[] = new int[nums.length];

        int left = 0;
        int right = nums.length - 1;

        for (int i = nums.length - 1; i >= 0; i--) {
            int leftSquare = nums[left] * nums[left];
            int rightSquare = nums[right] * nums[right];

            if (rightSquare > leftSquare) {
                output[i] = rightSquare;
                right--;
            } else {
                output[i] = leftSquare;
                left++;
            }
        }

        return output;
    }
}
