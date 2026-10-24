public class AverageCalculator {
    public AverageCalculator() {
    }

    public double calculateAverage(int[] values) {
        double sum = 0;
        for (int value : values) {
            sum += value;
        }
        return sum / values.length;
    }
}
