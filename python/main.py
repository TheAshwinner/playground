# Usage: `python3 python/main.py`
from people.person import Person
from concurrency_parallelism import (
    async_playground,
    producer_consumer_queue,
    conway_game_of_life,
)
import random_tricks
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
    # async_playground.raising_exception_in_thread()
    conway_game_of_life.run_game_standard(5, 5)
    conway_game_of_life.run_game_locked(5, 5)
    conway_game_of_life.run_game_pooled(5, 5)
    conway_game_of_life.run_game_coroutine(5, 5)


def create_and_update_person():
    mom = Person(
        name="test test",
        frequency=7,
        last_chat_date=datetime.datetime(year=2023, month=7, day=1),
        notes="Mom",
    )
    mom.update_last_chat(datetime.datetime(year=2023, month=7, day=7))
    print(mom.next_chat_date())


def main():
    print("Hello, world!")

    create_and_update_person()

    create_subprocess()
    print(random_tricks.find_longest_name(["Ashwin", "John", "Samuel", "Strauss"]))
    random_tricks.walrus_tester()
    random_tricks.list_comprehension()
    random_tricks.sort_priority_tester()
    random_tricks.v_arg_tester()


if __name__ == "__main__":
    main()
