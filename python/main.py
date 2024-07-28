# Usage: `python3 python/main.py`
from typing import Sequence, Optional
from people.person import Person
from concurrency_parallelism import (
    async_playground,
    producer_consumer_queue,
    conway_game_of_life,
)
import random_tricks
import datetime
import time
import os


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


def api(num: int, new_str: Optional[str], names: list[str]):
    print(num, new_str, names)


def main():
    print("Hello, world!")

    create_and_update_person()

    create_subprocess()
    print(random_tricks.find_longest_name(["Ashwin", "John", "Samuel", "Strauss"]))
    random_tricks.walrus_tester()
    random_tricks.list_comprehension()
    random_tricks.sort_priority_tester()
    random_tricks.v_arg_tester()
    test_seq: Sequence[str] = ["test"]
    if test_seq:
        print("if test_seq printed")
    if len(test_seq) >= 1:
        print("if len(test_seq) >=0:")

    print(str(int(time.time())))
    print(datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y_%m_%d_%H_%M_%S"))
    string = os.path.join("test", "test2")
    print(string)

    # api(4, ["hello", "hi"])
    random_tricks.generator_testing()


if __name__ == "__main__":
    main()
