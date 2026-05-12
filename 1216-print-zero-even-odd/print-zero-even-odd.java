class ZeroEvenOdd {
    private int n;
    private int state = 0;      // 0, 1, 2

    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            synchronized(this) {
                while (state != 0) {
                    this.wait();
                }
                if (i % 2 == 0) {
                    state = 1;
                } else {
                    state = 2;
                }
                printNumber.accept(0);
                this.notifyAll();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i < n + 1; i += 2) {
            synchronized(this) {
                while (state != 2) {
                    this.wait();
                }
                printNumber.accept(i);
                state = 0;
                this.notifyAll();
            }
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i < n + 1; i += 2) {
            synchronized(this) {
                while (state != 1) {
                    this.wait();
                }
                printNumber.accept(i);
                state = 0;
                this.notifyAll();
            }
        }
    }
}