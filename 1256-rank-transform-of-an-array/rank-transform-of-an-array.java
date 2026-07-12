class Solution {
    public int[] arrayRankTransform(int[] arr) {
        TreeMap<Integer, Integer> rankMap = new TreeMap<>();

        for (int num : arr) {
            rankMap.put(num, 0);
        }
        int rank = 1;
        for (int num : rankMap.keySet()) {
            rankMap.put(num, rank++);
        }

        return Arrays.stream(arr).map(rankMap::get).toArray();
    }
}