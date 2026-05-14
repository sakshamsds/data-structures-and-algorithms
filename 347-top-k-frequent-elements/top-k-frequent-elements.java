class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // min heap of size k, if size grows, pop smaller elements
        Queue<Integer> kFrequent = new PriorityQueue<>(
            (a, b) -> freqMap.get(a) - freqMap.get(b)
        );

        for (int key : freqMap.keySet()) {
            kFrequent.offer(key);
            if (kFrequent.size() > k) {
                kFrequent.poll();
            }
        }

        int[] answer = new int[k];
        for (int i = 0; i < k; i++) {
            answer[i] = kFrequent.poll();
        }

        return answer;
    }
}