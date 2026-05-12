class Solution {
    public int[] topKFrequent(int[] nums, int k) {  
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        Queue<Integer> pq = new PriorityQueue<>(
            (a, b) -> freqMap.get(a) - freqMap.get(b)
        );

        for (int n : freqMap.keySet()) {
            pq.add(n);
            if (pq.size() > k) pq.poll();
        }

        int[] top = new int[k];
        for (int i = k - 1; i >= 0; i--) {
            top[i] = pq.poll();
        }
        return top;
    }
}