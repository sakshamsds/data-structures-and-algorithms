class BoundedBlockingQueue {

    private int capacity;
    private Deque<Integer> boundedQueue;

    public BoundedBlockingQueue(int capacity) {
        boundedQueue = new ArrayDeque<>();
        this.capacity = capacity;
    }
    
    public synchronized void enqueue(int element) throws InterruptedException {
        while (boundedQueue.size() == capacity) {
            wait();
        }
        boundedQueue.offerLast(element);
        notifyAll();
    }
    
    public synchronized int dequeue() throws InterruptedException {
        while (boundedQueue.isEmpty()) {
            wait();
        }
        int last = boundedQueue.pollFirst();
        notifyAll();
        return last;
    }
    
    public int size() {
        return boundedQueue.size();
    }
}