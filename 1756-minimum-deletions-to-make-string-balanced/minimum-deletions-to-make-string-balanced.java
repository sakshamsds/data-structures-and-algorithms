/*
    aabaabbab
    aa aabb b
    left a
    right b
    a   a   b   a   a   b   b   a   b
0a  5a
0b  4b
    1a  4a
    0b  4b
                    4a  1a
                    1b  3b
*/

class Solution {
    public int minimumDeletions(String s) {
        int suffix_a = 0;
        for (char c : s.toCharArray()) {
            suffix_a += (c == 'a') ? 1 : 0;
        }
        int prefix_b = 0;

        int min_deletions = prefix_b + suffix_a;
        for (char c : s.toCharArray()) {
            if (c == 'a') {
                suffix_a--;
            } else {
                prefix_b++;
            }
            min_deletions = Math.min(min_deletions, prefix_b + suffix_a);
        }
        return min_deletions;        
    }
}