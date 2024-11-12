"""Задание No4
📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3- я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.
📌 Логируйте ошибки, если текст не соответсвует формату."""


import time
import re
from datetime import datetime, timedelta
import logging
import argparse

logger = logging.getLogger("date_text_to_datetime")
handler = logging.StreamHandler()
handler.setLevel(logging.ERROR)
formatter = logging.Formatter('{asctime} - {levelname}: {msg}', style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

date_text = '4th Wednesday of December'
target_year = 2024
def date_text_to_datetime(date_text: str, target_year: int):
    # Extract the ordinal number, weekday, and month using regex
    match = re.match(r'(\d)(?:st|nd|rd|th) (\w+) of (\w+)', date_text)
    if match:
        ordinal = int(match.group(1))
        weekday_str = match.group(2)
        month_str = match.group(3)

        # Convert weekday and month strings to corresponding integer values
        weekday = time.strptime(weekday_str, '%A').tm_wday  # 0 = Monday, 1 = Tuesday, etc.
        month = time.strptime(month_str, '%B').tm_mon
        # 1 = January, 12 = December

        # Find the first day of the target month and year
        first_of_month = datetime(target_year, month, 1)

        # Find the first occurrence of the specified weekday in the month
        days_until_weekday = (weekday - first_of_month.weekday() + 7) % 7
        first_weekday = first_of_month + timedelta(days=days_until_weekday)

        # Calculate the target weekday based on the ordinal (e.g., 4th Wednesday)
        target_date = first_weekday + timedelta(weeks=ordinal - 1)
        print(target_date)
    else:
        logger.error("Not correct format of date provided.")


date_text_to_datetime('4th Wednesday of December', 2024)

if __name__ == '__main__':
    pass
