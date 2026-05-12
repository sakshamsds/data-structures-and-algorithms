class ZeroEvenOdd {
    private int n;
    private AtomicInteger atomicInteger = new AtomicInteger(0);
    
    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            while (atomicInteger.get() != 0) {}
            printNumber.accept(0);
            if (i % 2 == 0) {
                atomicInteger.set(1);
            } else {
                atomicInteger.set(2);
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= n; i += 2) {
            while (atomicInteger.get() != 2) {}
            printNumber.accept(i);
            atomicInteger.set(0);
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i += 2) {
            while (atomicInteger.get() != 1) {}
            printNumber.accept(i);
            atomicInteger.set(0);
        }
    }
}