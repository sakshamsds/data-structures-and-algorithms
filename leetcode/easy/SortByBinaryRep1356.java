package easy;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class SortByBinaryRep1356 {

    Map<Integer, Integer> map = new HashMap<>();

    public static void main(String[] args) {
        // System.out.println(numberOfOnes(1));
        // System.out.println(numberOfOnes(2));
        // System.out.println(numberOfOnes(4));
        // System.out.println(numberOfOnes(8));
        // System.out.println(numberOfOnes(3));

        System.out.println(
                Arrays.toString(new SortByBinaryRep1356()
                        .sortByBits(new int[] { 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1 })));
        // System.out.println(
        // Arrays.toString(new SortByBinaryRep1356().sortByBits(new int[] { 0, 1, 2, 3,
        // 4, 5, 6, 7, 8 })));

    }

    public int[] sortByBits(int[] arr) {

        // make a hashmap, store number of 1
        for (int i = 0; i < arr.length; i++) {
            map.put(arr[i], numberOfOnes(arr[i]));
        }

        // sort
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (compare(arr[i], arr[j])) {
                    // compare i with j
                    // if i is larger than j => swap
                    arr[i] = arr[j] + arr[i] - (arr[j] = arr[i]);
                }
                // else move on
            }
        }
        return arr;
    }

    public boolean compare(int i, int j) {
        int zerosInI = map.get(i);
        int zerosInJ = map.get(j);
        if (zerosInI == zerosInJ) {
            return i > j;
        } else {
            return zerosInI > zerosInJ;
        }
    }

    public static int numberOfOnes(int x) {
        int count = 0;
        while (x != 0) {
            if (x % 2 == 1) {
                count++;
            }
            x = x / 2;
        }
        return count;
    }

}
