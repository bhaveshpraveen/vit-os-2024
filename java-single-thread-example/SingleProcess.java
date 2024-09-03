// SingleProcess.java

public class SingleProcess {
    public static void main(String[] args) {

        // Get the start time
        long startTime = System.currentTimeMillis();


        long sum = 0;
        for (long i = 0; i < 100_000_000_000L; i++) {
            sum += i;
        }

        // Get the end time
        long endTime = System.currentTimeMillis();

        // Calculate the elapsed time
        long elapsedTime = endTime - startTime;
        System.out.println("Total execution time: " + elapsedTime + " milliseconds");

    }
}