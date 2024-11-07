"""Задача 3. Счастливое число
Напишите программу, которая запрашивает у пользователя число до тех пор, пока сумма этих чисел не станет больше либо
равна 777. Каждое введенное число при этом дозаписывается в файл. Сделайте так, чтобы перед дозаписью программа с
вероятностью 1 к 13 выбрасывала пользователю случайное исключение и завершалась."""

from pathlib import Path
import random
import os

def main(file: Path):
    sum_of_nums = 0
    target_num = 777
    while sum_of_nums < target_num:
        try:
            num = int(input("Enter an integer: "))
            sum_of_nums += num
            if random.randint(1, 13) == 1:
                raise random.choice([ValueError('Error1'), TypeError('Error2'), RuntimeError('Error3')])
            with open(file, mode='a+', encoding='utf-8') as f:
                print(num, file=f)
        except ValueError:
            print(f"Oops! That's not an integer.")

MAGIC_NUMBER = 777
class MagicFileProcessor:
    def __init__(self, filename):
        """Инициализация с именем файла и определение пути к
        файлу."""
        self.filename = filename
        self.file_path = self.get_file_path()
        self.magic_sum = 0

    def get_file_path(self):
        """Возвращает полный путь к файлу."""
        return Path().cwd() / self.file_name

    def is_exception_raise(self):
        """Возвращает True с вероятностью 1 из 13, чтобы имитировать
        ошибку."""
        return random.randint(1, 13) == 7

    def pre_init(self):
        """Удаляет файл, если он существует."""
        try:
            Path(self.file_path).unlink()
        except OSError as e:
            print(e)
            print('Данный файл не может быть удален')

    def process_input(self):
        """Обрабатывает ввод пользователя и записывает его в
        файл."""
        try:
            input_number = int(input('Введите число: '))
            self.magic_sum += input_number
            if self.is_exception_raise():
                raise Exception('Вас постигла неудача!')
            with open(self.file_path, 'a') as out_fd:
                out_fd.write(str(input_number) + '\n')

        except (ValueError, KeyboardInterrupt) as e:
            print(e)
            print('Возникли проблемы при вводе.')
            print('Попробуйте еще раз')

    def run(self):
        """Основной метод для запуска процесса обработки ввода."""
        self.pre_init()  # Удаляет старый файл, если он существует
        while self.magic_sum < MAGIC_NUMBER:
            self.process_input()
        print('Вы успешно выполнили условие для выхода из порочного'
              'цикла!')

# Запуск программы
if __name__ == "__main__":
    processor = MagicFileProcessor('out_file.txt')
    processor.run()
