from people.person import Person
from concurrency_parallelism import async_playground
import datetime

def create_subprocess():
    async_playground.create_subprocess()
    async_playground.create_sleeping_subprocess(5)

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
