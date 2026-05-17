class BoundedBlockingQueue {

    private Semaphore enqueSem;
    private Semaphore dequeSem;
    private Deque<Integer> queue;

    public BoundedBlockingQueue(int capacity) {
        enqueSem = new Semaphore(capacity);
        dequeSem = new Semaphore(0);
        queue = new ArrayDeque<>();
    }
    
    public void enqueue(int element) throws InterruptedException {
        enqueSem.acquire();
        queue.offerLast(element);        
        dequeSem.release();
    }
    
    public int dequeue() throws InterruptedException {
        dequeSem.acquire();
        int ret = queue.pollFirst();
        enqueSem.release(1);
        return ret;
    }
    
    public int size() {
        return queue.size();
    }
}