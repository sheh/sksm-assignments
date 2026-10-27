from threading import Thread, Lock, RLock, Barrier, Semaphore, Timer
import time


def lock_example():
    lock = Lock()
    
    def _worker():
        lock.acquire()
        print("Lock acquired")
        time.sleep(1)
        lock.release()
        print("Lock released")

    t1 = Thread(target=_worker)
    t2 = Thread(target=_worker)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def rlock_example():
    rlock = RLock()
    def _worker():
        # acquire the rlock twice
        rlock.acquire()
        rlock.acquire()
        time.sleep(1)
        rlock.release()

    t1 = Thread(target=_worker)
    start_time = time.time()
    t1.start()
    t1.join()
    return time.time() - start_time


def barie_example():
    barie = Barrier(2)
    results = [None, None]
    
    def _worker(idx):
        start_time = time.time()
        barie.wait()
        results[idx] = time.time() - start_time
    
    t1 = Thread(target=_worker, args=(0,))
    t2 = Thread(target=_worker, args=(1,))
    t1.start()
    # wait for 1 second so that t1 can stay the barie
    time.sleep(1)
    t2.start()
    t1.join()
    t2.join()
    return results


def semaphore_example():
    semaphore = Semaphore(2)
    results = [None, None, None]
    
    def _worker(idx):
        start_time = time.time()
        semaphore.acquire()
        results[idx] = time.time() - start_time
        time.sleep(1)
        semaphore.release()
    
    t1 = Thread(target=_worker, args=(0,))
    t2 = Thread(target=_worker, args=(1,))
    t3 = Thread(target=_worker, args=(2,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    return results


def timer_example():
    timer = Timer(2, lambda: print("Timer expired"))
    start_time = time.time()
    timer.start()
    timer.join()
    return time.time() - start_time