package easy;

import java.time.Duration;
import java.time.Instant;

// https://leetcode.com/problems/richest-customer-wealth/
// 1672. Richest Customer Wealth

public class RichestCustomerWealth1672 {
    public static void main(String[] args) {
        int[][] accounts = new int[][] { { 1, 2, 3 }, { 3, 2, 1 } };
        System.out.println(maximumWealth(accounts));
    }

    // public static int maximumWealth(int[][] accounts) {
    // Instant start = Instant.now();
    // int max = Arrays.stream(accounts).mapToInt(customer ->
    // Arrays.stream(customer).sum()).max().getAsInt();
    // Instant end = Instant.now();
    // Duration duration = Duration.between(start, end);
    // System.out.println("time in millis: " + duration.toMillis());

    // return max;
    // }

    public static int maximumWealth(int[][] accounts) {
        Instant start = Instant.now();

        int max = 0;
        for (int i = 0; i < accounts.length; i++) {
            int sum = 0;
            for (int j = 0; j < accounts[0].length; j++) {
                sum += accounts[i][j];
            }
            max = Math.max(max, sum);
        }

        Instant end = Instant.now();
        Duration duration = Duration.between(start, end);
        System.out.println("time in millis: " + duration.toMillis());

        return max;
    }

}
