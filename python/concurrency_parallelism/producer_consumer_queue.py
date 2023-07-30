from threading import Thread, Lock
import time
from collections import deque
import random
from queue import Queue


class MyQueue:
    """Basic implementation of a producer-consumer queue.

    Effective Python item 55
    It turns out there are at least 4 things wrong with this code.
    First, we're processing 1000 items after polling 3000+ times.
    This means that we're wasting a lot of CPU time for polling when
    the queue doesn't have any items. (Raising and catching IndexErrors.)

    Second, determining that the done_queue is complete requires a busy loop.

    Third, the run methods execute indefinitely.
    (Even after the queue completed, we were still polling the done_queue)

    Fourth, if the pipeline gets bottlenecked at a point, we could run into
    a situation where the memory of a thread blows up (more and more elements
    continuously added to a queue).

    """

    def __init__(self):
        self.lock = Lock()
        self.items = deque()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()


class Worker(Thread):
    def __init__(self, func, in_queue: MyQueue, out_queue: MyQueue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.lock = Lock()
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                time.sleep(0.01)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1


def run_producer_consumer():
    download_queue = MyQueue()
    resize_queue = MyQueue()
    upload_queue = MyQueue()
    done_queue = MyQueue()

    def download(item):
        return item * 2

    def resize(item):
        return item + 1

    def upload(item):
        return item / 2

    threads = [
        Worker(download, download_queue, resize_queue),
        Worker(resize, resize_queue, upload_queue),
        Worker(upload, upload_queue, done_queue),
    ]

    for thread in threads:
        thread.start()

    for _ in range(1000):
        download_queue.put(random.randint(0, 20))

    while len(done_queue.items) < 1000:
        pass

    processed = len(done_queue.items)
    polled = sum(worker.polled_count for worker in threads)
    print(f"Processed {processed} items and polled {polled} items.")


def run_basic_queue():
    my_queue = Queue()

    def consumer():
        print("Consumer waiting.")
        my_queue.get()
        print("Consuemr finished.")

    thread = Thread(target=consumer)
    thread.start()
    print("Producer putting.")
    my_queue.put(object())
    print("Producer done.")
    thread.join()


def run_basic_queue_with_buffer():
    my_queue = Queue(1)

    def consumer():
        print("Consumer waiting.")
        my_queue.get()
        print("Consumer got 1.")
        my_queue.get()
        print("Consumer got 2.")

    thread = Thread(target=consumer)
    thread.start()
    my_queue.put(object())
    print("Producer put 1.")
    my_queue.put(object())
    print("Producer put 2.")
    thread.join()


class CloseableQueue(Queue):
    SENTINEL = object()

    def __init__(self):
        super().__init__()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, func, in_queue: CloseableQueue, out_queue: CloseableQueue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


def run_closeable_queue():
    """Run the closeable producer consumer queue.

    This corresponds to item 55 in Effective Python.
    """
    download_queue = CloseableQueue()
    resize_queue = CloseableQueue()
    upload_queue = CloseableQueue()
    done_queue = CloseableQueue()

    def download(item):
        return item * 2

    def resize(item):
        return item + 1

    def upload(item):
        return item / 2

    threads = [
        StoppableWorker(download, download_queue, resize_queue),
        StoppableWorker(resize, resize_queue, upload_queue),
        StoppableWorker(upload, upload_queue, done_queue),
    ]

    for thread in threads:
        thread.start()

    print("Putting items in list.")
    for _ in range(1000):
        download_queue.put(random.randint(0, 20))
    print("Finished putting items in list.")

    download_queue.close()
    download_queue.join()
    print("Finished download queue.")
    resize_queue.close()
    resize_queue.join()
    print("Finished resize queue.")
    upload_queue.close()
    upload_queue.join()
    print("Finished upload queue.")

    for thread in threads:
        thread.join()

    print(f"Items finished processing. Total count {done_queue.qsize()}")
