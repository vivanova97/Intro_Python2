"""
📌 Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
📌 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
📌 Для простоты договоримся, что год может быть в диапазоне [1, 9999].
📌 Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
📌 Проверку года на високосность вынести в отдельную защищённую функцию.
"""

__all__ = ['date_exists']


def _leap_year_check(year: int) -> bool:
    """Checks if year is leap-year."""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def date_exists(date: str) -> bool: # My solution
    """Checks if date exists."""
    min_year = 1
    max_year = 9999
    day, month, year = list(map(int, date.strip().split('.')))
    if min_year <= year <= max_year:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= day <= 31:
                return True
            else:
                return False
        elif month in [4, 6, 9, 11]:
            if 1 <= day <= 30:
                return True
            else:
                return False
        elif month == 2:
            if 1 <= day <= 28:
                return True
            elif day == 29:
                return _leap_year_check(year)
    return False

def date_exists_GPT(date: str) -> bool: #ChatGPT solution
    """Checks if the date in DD.MM.YYYY format is valid."""
    min_year = 1
    max_year = 9999

    try:
        day, month, year = map(int, date.strip().split('.'))
    except ValueError:
        return False  # Incorrect date format

    if not (min_year <= year <= max_year):
        return False

    if month < 1 or month > 12:
        return False

    # Days in each month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        if _leap_year_check(year):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28

    return False


if __name__ == '__main__':
    print(date_exists('30.12.2024'))
    print(date_exists_GPT('30.12.2024'))
