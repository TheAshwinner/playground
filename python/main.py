from people.person import Person
import datetime

def main():
    print("Hello, world!")
    mom = Person(name="test test", frequency=7,
                 last_chat_date=datetime.datetime(year=2023, month=7, day=1),
                 notes="Mom")
    mom.update_last_chat(datetime.datetime(year=2023, month=7, day=7))
    print(mom.next_chat_date())

if __name__ == "__main__":
    main()
