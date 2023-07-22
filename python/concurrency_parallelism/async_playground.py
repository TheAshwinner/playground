import subprocess
import time
from threading import Thread, Lock

def create_subprocess():
    """Create a basic subprocess calling `echo`.

    Tip 52 in Effective Python.
    
    Raises:
        CalledProcessError: Exit code of error is non-zero
    """
    result = subprocess.run(['echo', 'hello from child'], capture_output=True,
                            encoding='utf-8')
    result.check_returncode()
    print(result.stdout)

def create_sleeping_subprocess(process_num: int):
    """Create sleeping subprocess.
    
    Tip 52 in Effective Python. Note that if this program was run concurrently,
    it would take 2*process_num seconds, as opposed to ~2 seconds that it does
    with using subprocess.Popen().
    """
    print('Beginning create_sleeping_subprocess()')
    start_time = time.time()
    sleep_procs: list[subprocess.Popen] = []
    for _ in range(process_num):
        proc = subprocess.Popen(['sleep', '2'])
        sleep_procs.append(proc)
    
    for proc in sleep_procs:
        proc.communicate()
    end_time = time.time()
    print(f'Finished create_sleeping_subprocess in {end_time-start_time:.3} seconds.')

def create_threads_for_blocking_io(sleep_time: int, io_call_count: int):
    """Create threads for blocking I/O and compare with no threads.

    Tip 53 in Effective Python. Threads are useful for concurrent
    programming (such as for blocking I/O), but not as much for
    parallelism. Some background: parallelism is hard for CPython
    because of the Global Interpreter Lock.
    """
    print('Begin create_threads_for_blocking_io()')
    def blocking_io(sleep_time: int):
        time.sleep(sleep_time)
    
    # Test out multiple blocking_io calls without threads.
    start_time_no_threads = time.time()
    for _ in range(io_call_count):
        blocking_io(sleep_time=sleep_time)
    end_time_no_threads = time.time()
    print(f'Total time for blocking io with no threads: '
          f'{end_time_no_threads - start_time_no_threads:.3}')

    # Test out multiple blocking_io calls with threads.
    start_time_threads = time.time()
    threads = []
    for _ in range(io_call_count):
        thread = Thread(target=blocking_io, args=[sleep_time])
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end_time_threads = time.time()
    print(f'Total time for blocking io with threads: '
          f'{end_time_threads - start_time_threads:.3}')
    print('Ending create_threads_for_blocking_io()')

# The following comes from item 54 in Effective Python:
# Use Lock to prevent data races in threads.
# TODO: replace this with metaclasses?
class Counter:
    """Counter class with no mutex."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        # Note that this is not an atomic operation in Python.
        self.count += 1

class LockedCounter:
    """LockedCounter class with mutex."""
    def __init__(self):
        self.count = 0
        self.lock = Lock()
    
    def increment(self):
        with self.lock:
            self.count += 1

def increment_counter(worker_count: int, increment_count: int):
    def worker(count: int, counter: Counter):
        for _ in range(count):
            counter.increment()

    my_counter = Counter()
    threads = []
    for _ in range(worker_count):
        thread = Thread(target=worker, args=[increment_count, my_counter])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    
    expected_count = worker_count * increment_count
    actual_count = my_counter.count
    print(f'Expected count: {expected_count}, actual count: {actual_count}')

# TODO: This function is redundant. Remove this once abstract class/metaclass
# has been introduced.
def increment_counter_with_mutex(worker_count: int, increment_count: int):
    def worker(count: int, counter: Counter):
        for _ in range(count):
            counter.increment()

    my_counter = LockedCounter()
    threads = []
    for _ in range(worker_count):
        thread = Thread(target=worker, args=[increment_count, my_counter])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    
    expected_count = worker_count * increment_count
    actual_count = my_counter.count
    print(f'Expected count: {expected_count}, actual count: {actual_count}')