"""Задание No4
📌 Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери
символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)"""

from delete_non_latin_symbols import delete_non_latin_symbols

class TestDeleteNonLatinSymbols:
    @staticmethod
    def test_no_change():
        assert delete_non_latin_symbols("hi my name is anna") == 'hi my name is anna'

    @staticmethod
    def test_lower_case():
        assert delete_non_latin_symbols("Hi my name is Anna") == 'hi my name is anna'

    @staticmethod
    def test_punctuation():
        assert delete_non_latin_symbols("hi my name is anna.") == 'hi my name is anna'

    @staticmethod
    def test_punctuation_diff_alphabet():
        assert delete_non_latin_symbols("Hi менia зоvyt...") == 'hi ia vyt'






