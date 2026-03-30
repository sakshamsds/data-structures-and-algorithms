/**
    a   b   c   d   b   a
    acb bda
    c   a   b   d   a   b
    cba adb
 */

class Solution {
    public boolean checkStrings(String s1, String s2) {
        int n = s1.length();
        int[] evenFreq = new int[26];
        int[] oddFreq = new int[26];

        for (int i = 0; i < n; i++){
            if (i % 2 == 1) {
                oddFreq[s1.charAt(i) - 'a']++;
                oddFreq[s2.charAt(i) - 'a']--;
            } else {
                evenFreq[s1.charAt(i) - 'a']++;
                evenFreq[s2.charAt(i) - 'a']--;
            }
        }

        for (int i = 0; i < 26; i++) {
            if (oddFreq[i] != 0 || evenFreq[i] != 0) return false;
        }
        return true;
    }
}