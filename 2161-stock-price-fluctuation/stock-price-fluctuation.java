class StockPrice {

    // ts -> price
    // hashmap, O(n)
    // hashmap + 3 PQ + lazy deletions, O(logn)
    // Treemap, ts -> price, ts

    private Map<Integer, Integer> prices;
    private Queue<Pair<Integer, Integer>> latestPQ;     // maxHeap -> ts, price
    private Queue<Pair<Integer, Integer>> maxPQ;        // maxHeap -> ts, price
    private Queue<Pair<Integer, Integer>> minPQ;        // minHeap -> ts, price

    public StockPrice() {
        prices = new HashMap<>();
        latestPQ = new PriorityQueue<>((a, b) -> Integer.compare(b.getKey(), a.getKey()));
        maxPQ = new PriorityQueue<>((a, b) -> Integer.compare(b.getValue(), a.getValue()));
        minPQ = new PriorityQueue<>((a, b) -> Integer.compare(a.getValue(), b.getValue()));
    }
    
    public void update(int timestamp, int price) {
        prices.put(timestamp, price);
        latestPQ.offer(new Pair(timestamp, price));
        maxPQ.offer(new Pair(timestamp, price));
        minPQ.offer(new Pair(timestamp, price));
    }
    
    public int current() {    
        return cleanAndGetTop(latestPQ);
    }
    
    public int maximum() {      
        return cleanAndGetTop(maxPQ);
    }
    
    public int minimum() {      
        return cleanAndGetTop(minPQ);
    }

    private int cleanAndGetTop(Queue<Pair<Integer, Integer>> pq) {
        while (!prices.get(pq.peek().getKey()).equals(pq.peek().getValue())) {
            pq.poll();
        }
        return pq.peek().getValue();
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