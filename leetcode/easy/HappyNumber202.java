package easy;

// https://leetcode.com/problems/happy-number/
// 202. Happy Number
// https://leetcode.com/problems/happy-number/discuss/519280/JAVA-(-100-)-using-less-Cycle-finding-algorithm-greater
// https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/

public class HappyNumber202 {

    public static void main(String[] args) {

        int n = 19;
        // int n = 2;
        System.out.println(isHappy(n));
    }

    public static boolean isHappy(int n) {

        // floyd's cycle finding algorithm
        // useful in cyclic scenarios

        int s = n; // this will go slow
        int f = n; // this will go twice as fast as slow one

        do {
            s = sumOfSquaresOfDigits(s);
            f = sumOfSquaresOfDigits(sumOfSquaresOfDigits(f));

            if (f == 1)
                return true;

        } while (s != f);

        return false;

        // // Solution 1: using hashset
        // Set<Integer> seen = new HashSet<>();

        // while (true) {

        // seen.add(n);
        // n = sumOfSquaresOfDigits(n);

        // if (seen.contains(n)) {
        // break;
        // }

        // }

        // return n == 1;
    }

    private static int sumOfSquaresOfDigits(int n) {
        // System.out.println(n);

        int sum = 0;

        while (n > 0) {
            int digit = n % 10;
            sum += Math.pow(digit, 2);
            n /= 10;
        }
        System.out.println(sum);
        return sum;

    }
}
