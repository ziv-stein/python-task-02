"""Picks a random date between two dates given by the user."""

import random
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"
MONDAY = 0
NO_VINAIGRETTE_MESSAGE = "אין לי ויניגרט!"


def no_vinnigrete(first_date: datetime, second_date: datetime) -> datetime:
    """
    Returns a random date between two dates.

    :param first_date: First date
    :param second_date: Second date
    :return: Random date in the range
    """
    start_seconds = int(min(first_date, second_date).timestamp())
    end_seconds = int(max(first_date, second_date).timestamp())
    random_seconds = random.randint(start_seconds, end_seconds)
    return datetime.fromtimestamp(random_seconds)


def main():
    """Reads two dates, prints a random date and checks for Monday."""
    try:
        first_date = datetime.strptime(input("Enter first date: "), DATE_FORMAT)
        second_date = datetime.strptime(input("Enter second date: "), DATE_FORMAT)
    except ValueError:
        print("Error: dates must be in YYYY-MM-DD format")
        return

    chosen_date = no_vinnigrete(first_date, second_date)
    print(chosen_date.strftime(DATE_FORMAT))

    if chosen_date.weekday() == MONDAY:
        print(NO_VINAIGRETTE_MESSAGE)


if __name__ == "__main__":
    main()
