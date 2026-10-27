import pytest
from sync_examples import lock_example, barie_example, semaphore_example, rlock_example, timer_example
import time


def test_lock_example():
    start_time = time.time()
    lock_example()
    assert 1.9 < time.time() - start_time < 2.1, "Lock example should take between 1.9 and 2.1 seconds"


def test_rlock_example():
    start_time = time.time()
    rlock_example()
    assert 0.9 < time.time() - start_time < 1.1, "RLock example should take between 0.9 and 1.1 seconds"


def test_barie_example():
    results = barie_example()
    assert len(results) == 2, "Barie example should return 2 results"
    assert 0.9 < results[0] < 1.1, "First result should be between 0.9 and 1.1 seconds"
    assert 0 < results[1] < 0.1, "Second result should be between 0 and 0.1 seconds"


def test_semaphore_example():
    results = semaphore_example()
    assert len(results) == 3, "Semaphore example should return 3 results"
    assert 0 < results[0] < 0.1, "First result should be between 0 and 0.1 seconds"
    assert 0 < results[1] < 0.1, "Second result should be between 0 and 0.1 seconds"
    assert 0.9 < results[2] < 1.1, "Third result should be between 0.9 and 1.1 seconds"


def test_timer_example():
    result = timer_example()
    assert 1.9 < result < 2.1, "Timer example should take between 1.9 and 2.1 seconds"