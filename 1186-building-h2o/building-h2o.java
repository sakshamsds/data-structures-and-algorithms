class H2O {

    private Semaphore hydrogenSemaphore = new Semaphore(2);
    private Semaphore oxygenSemaphore = new Semaphore(0);

    public H2O() {
        
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		hydrogenSemaphore.acquire(1);
        releaseHydrogen.run();
        oxygenSemaphore.release(1);
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        oxygenSemaphore.acquire(2);
		releaseOxygen.run();
        hydrogenSemaphore.release(2);
    }
}