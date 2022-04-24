package easy;

// https://leetcode.com/problems/verifying-an-alien-dictionary/
// 953. Verifying an Alien Dictionary

public class VerifyingAlienDict953 {
    public static void main(String[] args) {
        System.out.println(new VerifyingAlienDict953().isAlienSorted(new String[] { "hello", "leetcode" },
                "hlabcdefgijkmnopqrstuvwxyz"));
        System.out.println(new VerifyingAlienDict953().isAlienSorted(new String[] { "word", "world", "row" },
                "worldabcefghijkmnpqstuvxyz"));
        System.out.println(new VerifyingAlienDict953().isAlienSorted(new String[] { "apple", "app" },
                "abcdefghijklmnopqrstuvwxyz"));
        System.out.println(new VerifyingAlienDict953().isAlienSorted(new String[] { "hello", "hello" },
                "abcdefghijklmnopqrstuvwxyz"));
    }

    public boolean isAlienSorted(String[] words, String order) {
        for (int i = 0; i < words.length - 1; i++) {
            boolean isSorted = areTwoWordsSorted(words[i], words[i + 1], order);
            if (!isSorted) {
                return false;
            }
        }
        return true;
    }

    private boolean areTwoWordsSorted(String word1, String word2, String order) {
        int min = Math.min(word1.length(), word2.length());
        for (int i = 0; i < min; i++) {
            char c1 = word1.charAt(i);
            char c2 = word2.charAt(i);

            if (c1 == c2) {
                continue;
            }

            // c1 order < c2 order
            return order.indexOf(c1) < order.indexOf(c2);
        }

        // return true if 2nd is bigger word
        return word2.length() >= word1.length();
    }
}
