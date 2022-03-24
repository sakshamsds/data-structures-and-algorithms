package easy;

// https://leetcode.com/problems/largest-perimeter-triangle/
// 976. Largest Perimeter Triangle

import java.util.Arrays;

public class LargestPerimeterTriange {

    public static void main(String[] args) {

        int[] nums = { 2, 1, 2 };

        System.out.println(largestPerimeter(nums));
    }

    public static int largestPerimeter(int[] nums) {
        // 1, 2, 4, 4, 6, 7
        // sort the array
        // sum two smaller sides > larger side
        // consider bigger side as base and try to form triangle
        // start from right side

        Arrays.sort(nums);

        for (int i = nums.length - 1; i > 1; i--) {

            int larger = nums[i];
            int smaller1 = nums[i - 1];
            int smaller2 = nums[i - 2];

            if (larger < smaller1 + smaller2) {
                return larger + smaller1 + smaller2;
            }

        }

        return 0;
    }

}
