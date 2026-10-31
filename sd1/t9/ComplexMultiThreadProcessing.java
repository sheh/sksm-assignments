import java.util.Random;
import java.util.Arrays;


public class ComplexMultiThreadProcessing {
    private static final int SIZE = 1000000;
    private static final int[] data = new int[SIZE];
    private static volatile int sum = 0;

    public static void main(String[] args) {
        Random random = new Random();
        for (int i = 0; i < SIZE; i++) {
            data[i] = random.nextInt(100);
        }

        sum = Arrays.stream(data).parallel().sum();

        System.out.println("Sum of all elements: " + sum);
    }

    public static int getSum() {
        return sum;
    }

    public static int[] getData() {
        return data;
    }
}