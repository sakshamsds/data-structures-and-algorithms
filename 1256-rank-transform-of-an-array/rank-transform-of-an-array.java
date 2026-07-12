class Solution {
    
    private record Element(int val, int idx) {}

    public int[] arrayRankTransform(int[] arr) {
        Queue<Element> minHeap = new PriorityQueue<>(Comparator.comparingInt(e -> e.val));

        for (int i = 0; i < arr.length; i++) {
            minHeap.offer(new Element(arr[i], i));
        }

        int prev = Integer.MIN_VALUE;
        int rank = 0;

        while (!minHeap.isEmpty()) {
            Element cur = minHeap.poll();
            if (cur.val > prev) rank++;
            arr[cur.idx] = rank;
            prev = cur.val;
        }

        return arr;
    }
}