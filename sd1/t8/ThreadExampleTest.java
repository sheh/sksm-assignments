import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ThreadExampleTest {
    @Test
    public void twoThreadsIncrementCounterToTwoThousand() {
        ThreadExample.main(new String[0]);

        int counter = new ThreadExample().getCounter();
        assertEquals(200_000, counter);
    }
}
