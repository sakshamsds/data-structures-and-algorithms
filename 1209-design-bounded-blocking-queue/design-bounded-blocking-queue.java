class BoundedBlockingQueue {

    private int capacity;
    private Queue<Integer> queue;

    public BoundedBlockingQueue(int capacity) {
        this.queue = new ArrayDeque<>();
        this.capacity = capacity;
    }
    
    public synchronized void enqueue(int element) throws InterruptedException {
        while (queue.size() == capacity) {
            wait();
        }
        queue.offer(element);
        notifyAll();
    }
    
    public synchronized int dequeue() throws InterruptedException {
        while (queue.isEmpty()) {
            wait();
        }        
        int rem = queue.poll();
        notifyAll();
        return rem;
    }
    
    public synchronized int size() {
        return queue.size();
    }
}