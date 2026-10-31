public class ThreadExample {
    private static int counter = 0;

    public static void main(String[] args) {
        Runnable task = () -> {
            // 1000 was too small to see the effect of threading
            for (int i = 0; i < 100_000; i++) {
                incrementCounter();
            }
        };

        Thread thread1 = new Thread(task);
        Thread thread2 = new Thread(task);

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Counter: " + counter);
    }

    synchronized static void incrementCounter() {
        counter++;
    }

    public int getCounter() {
        return counter;
    }
}

