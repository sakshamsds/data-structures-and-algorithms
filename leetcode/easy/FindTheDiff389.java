package easy;

import java.util.Arrays;

// https://leetcode.com/problems/find-the-difference/
// 389. Find the Difference

public class FindTheDiff389 {
    public static void main(String[] args) {
        System.out.println(new FindTheDiff389().findTheDifference("abcd", "abcde"));
    }

    public char findTheDifference(String s, String t) {
        // sum of ascii values in t - sum of ascii values in s

        int[] chars = new int[26];
        System.out.println(Arrays.toString(chars));

        for (int i = 0; i < s.length(); i++) {
            chars[t.charAt(i) - 97]++;
            chars[s.charAt(i) - 97]--;
        }
        chars[t.charAt(s.length()) - 97]++;

        System.out.println(Arrays.toString(chars));

        for(int i=0; i<26; i++){
            if(chars[i]>0){
                return (char) (i+97);
            }
        }
        return 'x';
    }
}
