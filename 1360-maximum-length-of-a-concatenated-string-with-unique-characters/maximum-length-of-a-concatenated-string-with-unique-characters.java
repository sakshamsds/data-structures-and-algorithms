class Solution {
    public int maxLength(List<String> arr) {
        Set<Character> uniques = new HashSet<>();
        return backtrack(0, arr, uniques);
    }

    private int backtrack(int idx, List<String> arr, Set<Character> uniques) {
        int maxSize = uniques.size();
        if (idx == arr.size()) {
            return maxSize;
        }
        // loop over all the elements
        for (int j = idx; j < arr.size(); j++) {
            if (isUnique(arr.get(j)) && isDisjoint(arr.get(j), uniques)) {
                for (char c : arr.get(j).toCharArray()) {   // update the uniques
                    uniques.add(c);
                }
                maxSize = Math.max(maxSize, backtrack(j + 1, arr, uniques));
                for (char c : arr.get(j).toCharArray()) {   // remove from uniques
                    uniques.remove(c);
                }
            }
        }
        return maxSize;
    }

    private boolean isUnique(String str) {
        Set<Character> set = new HashSet<>();
        for (char c : str.toCharArray()) {
            if (!set.add(c)) {
                return false;
            }
        }
        return true;
    }

    private boolean isDisjoint(String str, Set<Character> uniques) {
        for (char c : str.toCharArray()) {
            if (uniques.contains(c)) {      
                return false;
            }
        }
        return true;
    }
}