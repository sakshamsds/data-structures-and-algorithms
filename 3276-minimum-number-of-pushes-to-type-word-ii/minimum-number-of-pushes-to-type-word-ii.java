class Solution {
    public int minimumPushes(String word) {
        int[] freqs = new int[26];
        for (char c : word.toCharArray()) {
            freqs[c - 'a']++;
        }
        
        Arrays.sort(freqs);
        // System.out.println(Arrays.toString(freqs));
        int pushes = 0;
        for (int i = 25; i >= 0; i--) {
            pushes += freqs[i] * (((25 - i) / 8) + 1);
        }

        return pushes;
    }
}