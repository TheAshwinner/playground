from unittest import TestCase, main
from person import Person
import datetime


class PersonTestCase(TestCase):
    def testNextChat(self):
        last_chat_date = datetime.datetime(year=2023, month=6, day=1)
        user = Person(
            name="Test Name", frequency=10, last_chat_date=last_chat_date, notes="notes"
        )
        self.assertEqual(
            user.next_chat_date(), datetime.datetime(year=2023, month=6, day=11)
        )

    def testUpdateLastChat(self):
        last_chat_date = datetime.datetime(year=2023, month=6, day=1)
        user = Person(
            name="Test Name", frequency=10, last_chat_date=last_chat_date, notes="notes"
        )
        user.update_last_chat(
            last_chat_date=datetime.datetime(year=2023, month=7, day=1)
        )
        self.assertEqual(
            user.next_chat_date(), datetime.datetime(year=2023, month=7, day=11)
        )

    def testUpdateLastChatOld(self):
        last_chat_date = datetime.datetime(year=2023, month=6, day=1)
        user = Person(
            name="Test Name", frequency=10, last_chat_date=last_chat_date, notes="notes"
        )
        very_old_chat = datetime.datetime(year=2022, month=6, day=1)
        user.update_last_chat(very_old_chat)
        self.assertEqual(
            user.next_chat_date(), datetime.datetime(year=2023, month=6, day=11)
        )


if __name__ == "__main__":
    main()
