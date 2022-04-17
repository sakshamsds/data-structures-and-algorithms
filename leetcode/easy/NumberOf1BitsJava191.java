package easy;

// https://leetcode.com/problems/number-of-1-bits/
// 191. Number of 1 Bits
// geeksforgeeks.org/count-set-bits-in-an-integer/

public class NumberOf1BitsJava191 {

    public static void main(String[] args) {
        int n = -3; // 1001
        System.out.println(Integer.toString(n, 2));
        System.out.println(Integer.toUnsignedString(n, 2));
        System.out.println(hammingWeight(n));
    }

    public static int hammingWeight(int n) {
        // Brian Kernighan’s Algorithm
        // while n>0, take & of n, n-1
        // this will unset all set bits
        // O(# set bits)
        int count = 0;

        while (n != 0) {
            n = n & (n - 1);
            count++;
        }

        return count;
    }

}
