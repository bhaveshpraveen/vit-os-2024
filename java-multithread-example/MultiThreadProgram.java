public class MultiThreadProgram {
    public static void main(String[] args) {
        // Get the start time
        long startTime = System.currentTimeMillis(); // Or use System.nanoTime() for higher precision

        // find out the number of cores
	    int numCores = Runtime.getRuntime().availableProcessors();
        System.out.println("Available Cores: " + numCores);

        // Create an array to hold the threads and workers
        int numThreads = numCores;
        Thread[] threads = new Thread[numThreads];

        for (int i = 0; i < numThreads; i++) {
            Thread thread = new Thread(new Worker(), "Thread-" + i);
            threads[i] = thread;
            threads[i].start();
        }

        // Wait for all threads to finish
        for (Thread thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                System.out.println(e);
            }
            
        }

        // Get the end time
        long endTime = System.currentTimeMillis(); // Or use System.nanoTime()

        // Calculate the elapsed time
        long elapsedTime = endTime - startTime;

        System.out.println("Total execution time: " + elapsedTime + " milliseconds");

    }
}

class Worker implements Runnable {

    @Override
    public void run() {   
        String threadName = Thread.currentThread().getName();
        System.out.println(threadName + " started.");
        // Perform a CPU-intensive task
        long sum = 0;
        for (long i = 0; i < 10_000_000_000L; i++) {
            sum += i;
        }
        System.out.println(threadName + " finished. Sum: " + sum);

    }
}
