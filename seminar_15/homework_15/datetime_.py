"""Напишите скрипт, который получает текущее время и дату, а затем выводит их в формате YYYY-MM-DD HH:MM:SS.
Дополнительно, выведите день недели и номер недели в году."""

from datetime import datetime

dt_now = datetime.now()
print(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
print(dt_now.strftime('Day of the week: %A \nWeek of the year: %W'))
