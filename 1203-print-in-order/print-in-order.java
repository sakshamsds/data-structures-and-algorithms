class Foo {

    private AtomicInteger jobNumber = new AtomicInteger(1);

    public Foo() {
        
    }

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        jobNumber.incrementAndGet();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        while (jobNumber.get() != 2){}
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        jobNumber.incrementAndGet();
    }

    public void third(Runnable printThird) throws InterruptedException {
        while (jobNumber.get() != 3){}
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}