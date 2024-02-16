class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> freqs = new HashMap<>();
        for (int num : arr) {
            freqs.put(num, freqs.getOrDefault(num, 0) + 1);
        }
        int[] buckets = new int[arr.length + 1];
        for (Map.Entry<Integer, Integer> e : freqs.entrySet()) {
            buckets[e.getValue()]++;
        }
        int uniques = freqs.size();
        for (int i = 1; i < buckets.length; i++) {
            int numElements = i * buckets[i];
            if (k > numElements) {
                k -= numElements;
                uniques -= buckets[i];
            } else {
                return uniques - (k / i);
            }
        }
        return -1;
    }
}