import doctest


"""Задание No1
📌 Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
📌 Возвращается строка в нижнем регистре."""

"""Задание No2
📌 Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери
символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)"""


def delete_non_latin_symbols(text: str) -> str:
    """Deletes all non-latin and non-space symbols from text.
    >>> delete_non_latin_symbols("hi my name is anna")
    'hi my name is anna'
    >>> delete_non_latin_symbols("Hi my name is Anna")
    'hi my name is anna'
    >>> delete_non_latin_symbols("Hi менia зоvyt...")
    'hi ia vyt'
    >>> delete_non_latin_symbols("hi my name is anna.")
    'hi my name is anna'

    """
    import string
    text = text.lower()

    for symbol in text:
        if symbol not in string.ascii_lowercase and symbol != ' ':
            text = text.replace(symbol,'')
    return text


if __name__ == '__main__':
    doctest.testmod(verbose=True) # or this command in terminal: python3 -m doctest ./delete_non_latin_symbols.py -v

