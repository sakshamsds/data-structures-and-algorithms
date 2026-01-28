class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> idxMap = new HashMap<>();
        int longest = 0;
        int l = 0;

        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            if (idxMap.containsKey(c)) {
                l = Math.max(idxMap.get(c) + 1, l);
            } 
            longest = Math.max(longest, r - l + 1);
            idxMap.put(c, r);      
        }
        return longest;
    }
}