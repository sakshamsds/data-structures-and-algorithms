package easy;

// https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
// 1523. Count Odd Numbers in an Interval Range

public class CountOddNumbersInIntervalRange {

    public static void main(String[] args) {
        int low = 8;
        int high = 10;
        System.out.println(countOdds(low, high));
    }

    public static int countOdds(int low, int high) {
        // both odd, 5-3 / 2 + 1; 3, 5
        // both even, 6-2 / 2; 3, 5
        // one even, 6-1 / 2 + 1; 1, 3, 5

        if (low % 2 == 0 && high % 2 == 0) {
            return (high - low) / 2;
        }
        return (high - low) / 2 + 1;
    }
}
