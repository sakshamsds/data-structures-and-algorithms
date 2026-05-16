class StockPrice {

    // ts -> price
    // hashmap, O(n)
    // hashmap + 2 PQ + lazy deletions, O(logn)
    // Treemap, ts -> price, ts

    private Map<Integer, Integer> prices;
    private Queue<int[]> maxPQ;        // maxHeap -> ts, price
    private Queue<int[]> minPQ;        // minHeap -> ts, price
    private int latestTS;

    public StockPrice() {
        prices = new HashMap<>();
        latestTS = 0;
        maxPQ = new PriorityQueue<>((a, b) -> Integer.compare(b[1], a[1]));
        minPQ = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));
    }
    
    public void update(int timestamp, int price) {
        prices.put(timestamp, price);
        latestTS = Math.max(timestamp, latestTS);
        maxPQ.offer(new int[]{timestamp, price});
        minPQ.offer(new int[]{timestamp, price});
    }
    
    public int current() {    
        return prices.get(latestTS);
    }
    
    public int maximum() {      
        return cleanAndGetTop(maxPQ);
    }
    
    public int minimum() {      
        return cleanAndGetTop(minPQ);
    }

    private int cleanAndGetTop(Queue<int[]> pq) {
        while (prices.get(pq.peek()[0]) != pq.peek()[1]) {
            pq.poll();
        }
        return pq.peek()[1];
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.update(timestamp,price);
 * int param_2 = obj.current();
 * int param_3 = obj.maximum();
 * int param_4 = obj.minimum();
 */