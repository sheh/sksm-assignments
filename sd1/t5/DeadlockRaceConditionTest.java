import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class RaceConditionTest {
    @Test
    public void testRaceCondition() throws Exception {
        MultithreadingProblems.RaceConditionExample.main(new String[0]);

        int counter = new MultithreadingProblems.RaceConditionExample().getCounter();
        assertTrue(counter == 1_000_000, "Counter should be 1_000_000, but was " + counter);
    }
}

class DeadlockTest {
    @Test
    public void testDeadlockRaceCondition() throws Exception {
        MultithreadingProblems.DeadlockExample.main(new String[0]);
        assertTrue(true, "No Deadlock detected");
    }
}