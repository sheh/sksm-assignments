import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AverageCalculatorTest {
    @Test
    public void calculateAverageOfSeveralValues() {
        AverageCalculator calculator = new AverageCalculator();
        double average = calculator.calculateAverage(new int[]{1, 2, 3, 4});
        assertEquals(2.5, average, 0.0001);
    }

    @Test
    public void calculateAverageOfSingleValue() {
        AverageCalculator calculator = new AverageCalculator();
        assertEquals(7.0, calculator.calculateAverage(new int[]{7}), 0.0001);
    }

    @Test
    public void calculateAverageWithNegativesAndZero() {
        AverageCalculator calculator = new AverageCalculator();
        assertEquals(0.0, calculator.calculateAverage(new int[]{-2, 0, 2}), 0.0001);
    }

    @Test
    public void calculateAverageEmptyArray() {
        AverageCalculator calculator = new AverageCalculator();
        assertEquals(0.0, calculator.calculateAverage(new int[]{}), 0.0001);
    }

}
