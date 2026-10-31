import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ComplexMultiThreadProcessingTest {
    @Test
    public void parallelSumMatchesSequentialSum() {
        ComplexMultiThreadProcessing.main(new String[0]);

        int expected = 0;
        for (int value : ComplexMultiThreadProcessing.getData()) {
            expected += value;
        }

        assertEquals(expected, ComplexMultiThreadProcessing.getSum());
    }
}
