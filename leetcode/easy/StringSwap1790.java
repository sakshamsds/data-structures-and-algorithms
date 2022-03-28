package easy;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
// 1790. Check if One String Swap Can Make Strings Equal

public class StringSwap1790 {

    public static void main(String[] args) {
        String s1 = "bank";
        String s2 = "kanb";

        System.out.println(areAlmostEqual(s1, s2));

    }

    public static boolean areAlmostEqual(String s1, String s2) {

        // 0 swap, check for equality
        if (s1.equals(s2)) {
            return true;
        }

        // 1 swap, errors at two places exactly, containing same letters
        List<Integer> idx = new ArrayList<>();

        int countErrors = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                countErrors++;
                idx.add(i);
            }
        }

        if (countErrors == 2) {
            return s1.charAt(idx.get(0)) == s2.charAt(idx.get(1)) && s1.charAt(idx.get(1)) == s2.charAt(idx.get(0));
        }

        return false;
    }

}
