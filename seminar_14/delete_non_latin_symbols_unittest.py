"""Задание No3
📌 Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери
символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)"""

import unittest
from delete_non_latin_symbols import delete_non_latin_symbols

class TestDeleteNonLatin(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual(delete_non_latin_symbols("hi my name is anna"), 'hi my name is anna')

    def test_lower(self):
        self.assertEqual(delete_non_latin_symbols("Hi my name is Anna"), 'hi my name is anna')

    def test_delete_punctuation(self):
        self.assertEqual(delete_non_latin_symbols("Hi менia зоvyt..."),  'hi ia vyt')


if __name__ == '__main__':
    unittest.main(verbosity=2)

