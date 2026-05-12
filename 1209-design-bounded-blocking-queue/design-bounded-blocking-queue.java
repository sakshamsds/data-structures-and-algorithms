class BoundedBlockingQueue {
    private Semaphore enqueSem;
    private Semaphore dequeSem;
    Queue<Integer> queue;
    int capacity;

    public BoundedBlockingQueue(int capacity) {
        queue = new ArrayDeque<>();
        this.capacity = capacity;
        enqueSem = new Semaphore(capacity);
        dequeSem = new Semaphore(0);
    }
    
    public void enqueue(int element) throws InterruptedException {
        enqueSem.acquire();
        queue.offer(element);
        dequeSem.release();
    }
    
    public int dequeue() throws InterruptedException {
        dequeSem.acquire();
        int ret = queue.poll();
        enqueSem.release();
        return ret;
    }   
    
    public int size() {
        return queue.size();
    }
}