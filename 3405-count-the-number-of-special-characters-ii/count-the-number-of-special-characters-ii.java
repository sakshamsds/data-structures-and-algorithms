class Solution {
    public int numberOfSpecialChars(String word) {
        int[] lowerIdxs = new int[26];
        int[] upperIdxs = new int[26];
        Arrays.fill(lowerIdxs, -1);
        Arrays.fill(upperIdxs, -1);

        // int[] lowerIdxs = IntStream.generate(() -> -1).limit(26).toArray();
        // int[] upperIdxs = IntStream.generate(() -> -1).limit(26).toArray();

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (Character.isLowerCase(c)) {
                lowerIdxs[c - 'a'] = i;
            } else if (upperIdxs[c - 'A'] == -1) {
                upperIdxs[c - 'A'] = i;
            }
        }

        int special = 0;
        for (int i = 0; i < 26; i++) {
            if (lowerIdxs[i] > -1 && lowerIdxs[i] < upperIdxs[i]) special++;
        }
        return special;
    }
}