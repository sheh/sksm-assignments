import java.util.concurrent.atomic.AtomicInteger;


class MultithreadingProblems {


    public static class RaceConditionExample {
        
        private static AtomicInteger counter = new AtomicInteger(0);

        public static void main(String[] args) {
            int numberOfThreads = 10;
            Thread[] threads = new Thread[numberOfThreads];

            for (int i = 0; i < numberOfThreads; i++) {
                threads[i] = new Thread(() -> {
                    for (int j = 0; j < 100_000; j++) {
                        // before it was incrementing counter directly, now it is using AtomicInteger
                        // so it was not thread safe
                        counter.incrementAndGet();
                    }
                });
                threads[i].start();
            }

            for (int i = 0; i < numberOfThreads; i++) {
                try {
                    threads[i].join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            System.out.println("Final counter value: " + counter);
        }
        public int getCounter() {
            return counter.get();
        }
    }

    public static class DeadlockExample {
        // the locks should be the same for both threads, so that they can acquire the locks in the same order
        private static final Object lock1 = new Object();
        private static final Object lock2 = new Object();

        public static void main(String[] args) {
            Thread thread1 = new Thread(() -> {
                synchronized (lock1) {
                    System.out.println("Thread 1 acquired lock1");

                    try { Thread.sleep(50); } 
                    catch (InterruptedException e) { e.printStackTrace(); }

                    synchronized (lock2) {
                        System.out.println("Thread 1 acquired lock2");
                    }
                }
            });

            Thread thread2 = new Thread(() -> {
                synchronized (lock1) {
                    System.out.println("Thread 2 acquired lock1");

                    try { Thread.sleep(50); } 
                    catch (InterruptedException e) { e.printStackTrace(); }

                    synchronized (lock2) {
                        System.out.println("Thread 2 acquired lock2");
                    }
                }
            });

            thread1.start();
            thread2.start();

            try {
                thread1.join();
                thread2.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println("Finished");
        }
    }
}