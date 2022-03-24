package easy;

import java.util.HashSet;
import java.util.Set;

// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
// 1502. Can Make Arithmetic Progression From Sequence
// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/discuss/720253/JavaPython-3-O(n)-and-O(nlogn)-codes-w-brief-explanation-and-analysis.

public class SequenceToArithmetic {

    public static void main(String[] args) {

        int[] sequence = { 0, 0, 1 };
        // int[] sequence = { 3, 5, 1 };
        System.out.println(canMakeArithmeticProgression(sequence));

    }

    public static boolean canMakeArithmeticProgression(int[] arr) {

        // O(n)
        // Hashset.contains() - O(1)
        // ArrayList.contains() - O(n)

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        Set<Integer> sequenceSet = new HashSet<>();

        for (int num : arr) {
            sequenceSet.add(num);
            max = Math.max(max, num);
            min = Math.min(min, num);
        }

        // covering edge test cases
        if ((max - min) % (arr.length - 1) != 0) {
            return false;
        }

        int diff = (max - min) / (arr.length - 1);

        int num = min;

        for (int i = 1; i < arr.length - 1; i++) {
            num += diff;
            System.out.println(num);
            if (!sequenceSet.contains(num)) {
                return false;
            }
        }

        return true;

        // // O(logN)
        // Arrays.sort(arr);

        // int diff = arr[1] - arr[0];

        // for (int i = 1; i < arr.length - 1; i++) {

        // if (arr[i + 1] - arr[i] != diff) {
        // return false;
        // }

        // }

        // return true;
    }

}
