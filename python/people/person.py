import datetime


class Person:
    """Class representing person to chat with."""

    def __init__(
        self,
        name: str = "Unnamed",
        frequency: int = 365,
        last_chat_date: datetime.datetime = datetime.date.today,
        notes: str = None,
    ) -> None:
        self._name = name
        self._frequency = frequency
        self._last_chat_date = last_chat_date
        self._notes = notes
        self._next_chat_date = self._find_next_chat_date(
            last_chat_date=last_chat_date, frequency=frequency
        )

    def _find_next_chat_date(self, last_chat_date: datetime.datetime, frequency: int):
        """Compute the next date the user will chat with with this person."""
        return last_chat_date + datetime.timedelta(days=frequency)

    def update_last_chat(self, last_chat_date: datetime.datetime):
        """Update the last date that the user has chatted with this person."""
        if self._last_chat_date < last_chat_date:
            self._last_chat_date = last_chat_date
            self._next_chat_date = self._find_next_chat_date(
                last_chat_date, self._frequency
            )

    def next_chat_date(self) -> datetime.datetime:
        """Return the next chat date."""
        return self._next_chat_date

    def get_full_person_details(self):
        return (
            self._name,
            self._frequency,
            self._last_chat_date,
            self._notes,
            self._next_chat_date,
        )
