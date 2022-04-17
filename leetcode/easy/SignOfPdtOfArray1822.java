package easy;

// https://leetcode.com/problems/sign-of-the-product-of-an-array/
// 1822. Sign of the Product of an Array

public class SignOfPdtOfArray1822 {

    public static void main(String[] args) {
        int[] nums = { -1, -2, -3, -4, 3, 2, 1 };
        System.out.println(arraySign(nums));

    }

    public static int arraySign(int[] nums) {

        // 1. multiplication leads to overflow
        // 2. count negative numbers
        // 3. just invert the sign

        int sign = 1;

        for (int num : nums) {
            if (num == 0) {
                return 0;
            }

            if (num < 0) {
                sign = -sign;
            }
        }

        return sign;

    }
}
