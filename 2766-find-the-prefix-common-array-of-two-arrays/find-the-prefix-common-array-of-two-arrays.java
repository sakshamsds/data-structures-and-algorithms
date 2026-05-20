class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        // 2n - set().size();
        Set<Integer> uniques = new HashSet<>();
        int[] answer = new int[A.length];
        for (int i = 0; i < A.length; i++) {
            uniques.add(A[i]);
            uniques.add(B[i]);
            answer[i] = 2 * (i + 1) - uniques.size();
        }
        return answer;
    }
}