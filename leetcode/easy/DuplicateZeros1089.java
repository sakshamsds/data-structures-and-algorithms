package easy;

import java.util.Arrays;

// Meh
// https://www.youtube.com/watch?v=io3N5YTFbxM
// https://leetcode.com/problems/duplicate-zeros/
// 1089. Duplicate Zeros

public class DuplicateZeros1089 {
    public static void main(String[] args) {
        // int[] arr = new int[] { 1, 2, 3 };
        int[] arr = new int[] { 8, 4, 5, 0, 0, 0, 0, 7 };
        // int[] arr = new int[] { 1, 0, 2, 3, 0, 4, 5, 0 };
        new DuplicateZeros1089().duplicateZeros(arr);
        System.out.println(Arrays.toString(arr));
    }

    public void duplicateZeros(int[] arr) {
        int len = arr.length;
        int zeros = 0;
        for (int num : arr) {
            if (num == 0) {
                zeros++;
            }
        }

        // two pointers
        // first one starts at array length
        // second on starts at increased array length
        int i = len - 1;
        int j = len + zeros - 1;
        while (i != j) {
            if (j < len) {
                arr[j] = arr[i];
            }
            if (arr[i] == 0) {
                j--;
                if (j < len) {
                    arr[j] = arr[i];
                }
            }
            i--;
            j--;
        }
    }
}
