class H2O {

    private int hCount = 0;

    public H2O() {
        
    }

    public synchronized void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        while (hCount == 2) {
            wait();
        }
        releaseHydrogen.run();
        hCount++;
        notifyAll();
    }

    public synchronized void oxygen(Runnable releaseOxygen) throws InterruptedException {
        while (hCount < 2) {
            wait();
        }        
		releaseOxygen.run();
        hCount = 0;
        notifyAll();
    }
}