"""Напишите функцию, которая принимает количество дней от текущей даты и возвращает дату, которая наступит через
указанное количество дней. Дополнительно, выведите эту дату в формате YYYY-MM-DD"""

from datetime import date, timedelta, datetime


def task_planning(days_from_now: int) -> date:
    """Returns the date that is the given number of days from the current date.
    :param days_from_now: Number of days from today
    :return: Date in formate YYYY-MM-DD"""

    time_delta = timedelta(days=days_from_now)
    time_now = datetime.now()
    resulting_date = time_now + time_delta

    return resulting_date.date()


if __name__ == '__main__':
    print(task_planning(43))