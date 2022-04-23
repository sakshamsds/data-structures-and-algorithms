package easy;

// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
// 1588. Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/981968/Java-easy-solution-with-proper-explanation.
// lookout for prefix sum

public class SumOfOddLengthArrays1588 {
    public static void main(String[] args) {

        // int[] arr = new int[] { 1, 4, 2, 5, 3 };
        // int[] arr = new int[] { 1, 2 };
        int[] arr = new int[] { 10, 11, 12 };
        System.out.println(sumOddLengthSubarrays(arr));

        // 10
        // 11
        // 12
        // 10, 11, 12
        // no of sub arrays that start with 1 -> 1, 14, 142, 1425, 14253 = 5
        // no of sub arrays that end with 1 -> 1
        // total = 5*1 = 5; 1, 14, 142, 1425, 14253
        // odd freq = 5+1/2 = 3
        // no of sub arrays that start with 4 -> 4, 42, 425, 4256 = 4 = length-index
        // no of sub arrays that end with 4 -> 14, 4 = 2 = index+1
        // total = 4*2 = 8; 14, 142, 1425, 14256, 4, 42, 425, 4256
        // odd freq = 4*2 + 1/2
    }

    // For each element i of the passed array arr[], the solution to this problem is
    // to sum together all: arr[i] * (number of odd length subarrays that include
    // a[i])
    public static int sumOddLengthSubarrays(int[] arr) {
        int length = arr.length;
        int sum = 0;

        for (int i = 0; i < length; i++) {
            // int numStart = length - i;
            // int numEnd = i + 1;
            // // int totalFreq = numEnd * numStart;
            // int oddFreq = (numEnd * numStart + 1) / 2;
            // // if (totalFreq % 2 == 1) {
            // // oddFreq++;
            // // }
            // sum += arr[i] * oddFreq;

            sum += arr[i] * (((i + 1) * (length - i) + 1) / 2);
        }
        return sum;
    }
}
