package easy;

// 1837. Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

public class SumOfDigitsInBaseK1837 {
    public static void main(String[] args) {
        System.out.println(new SumOfDigitsInBaseK1837().sumBase(34, 6));

    }

    public int sumBase(int n, int k) {
        int sum = 0;

        while (n > 0) {
            sum += n % k;
            n = n / k;
        }

        return sum;
    }
}
