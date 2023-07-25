# Usage: `python3 python/main.py`
from people.person import Person
from concurrency_parallelism import async_playground, producer_consumer_queue
import datetime

def create_subprocess():
    # async_playground.create_subprocess()
    # async_playground.create_sleeping_subprocess(5)
    # async_playground.create_threads_for_blocking_io(sleep_time=1, io_call_count=5)
    # async_playground.increment_counter(worker_count=20, increment_count=100000)
    # async_playground.increment_counter_with_mutex(
    #     worker_count=20,increment_count=100000)
    # producer_consumer_queue.run_producer_consumer()
    # producer_consumer_queue.run_basic_queue()
    # producer_consumer_queue.run_basic_queue_with_buffer()
    # producer_consumer_queue.run_closeable_queue()
    async_playground.raising_exception_in_thread()

def create_and_update_person():
    mom = Person(name="test test", frequency=7,
                 last_chat_date=datetime.datetime(year=2023, month=7, day=1),
                 notes="Mom")
    mom.update_last_chat(datetime.datetime(year=2023, month=7, day=7))
    print(mom.next_chat_date())

def main():
    print("Hello, world!")
    
    create_and_update_person()

    create_subprocess()

if __name__ == "__main__":
    main()
