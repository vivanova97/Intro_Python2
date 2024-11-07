"""Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие
методы:
Атрибуты класса:
name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и
результатах тестов для каждого предмета в виде словаря.

Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. Если ФИО не соответствует условию,
выведите:
ФИО должно состоять только из букв и начинаться с заглавной буквы
"""
from audioop import avgpp

"""get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.
get_average_grade(self): Возвращает средний балл по всем предметам."""

import csv


class TitleString:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.param_name} accepts type str not {type(value)}.")
        if not value.istitle():
            raise ValueError(f"{self.param_name} should be formatted as a title, each new word starting with a capital "
                             f"letter.")
        setattr(instance, self.param_name, value)


class Student:
    name = TitleString()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = dict()
        self.subjects_file = self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        try:
            with open(f"{subjects_file}.csv", mode='r', newline='') as csv_f:
                csv_file = csv.DictReader(csv_f, fieldnames=["Математика","Физика","История","Литература"])
                for subject in csv_file.fieldnames:
                    self.subjects[subject] = dict()
        except FileNotFoundError:
            raise FileNotFoundError("File not found.")

    def add_grade(self, subject: str, grade: int):
        min_grade = 0
        max_grade = 5

        if subject not in self.subjects:
            raise KeyError(f"{subject} not found.")
        if not isinstance(grade, int) or not (min_grade <= grade <= max_grade):
            raise ValueError(f"Grade should be between {min_grade} and {max_grade}.")

        if "grades" not in self.subjects[subject]:
            self.subjects[subject]["grades"] = []
        self.subjects[subject]["grades"].append(grade)

    def add_test_score(self, subject: str, test_score: int):
        min_score = 0
        max_score = 100

        if subject not in self.subjects:
            raise KeyError(f"{subject} not found.")
        if not isinstance(test_score, int) or not (min_score <= test_score <= max_score):
            raise ValueError(f"Test score should be between {min_score} and {max_score}.")

        if "test_scores" not in self.subjects[subject]:
            self.subjects[subject]["test_scores"] = []
        self.subjects[subject]["test_scores"].append(test_score)

    def get_average_test_score(self, subject: str):
        return sum(self.subjects[subject]["test_scores"])/len(self.subjects[subject]["test_scores"])

    def get_average_grade(self):
        all_grades = [grade for subject in self.subjects.values() if "grades" in subject for grade in subject["grades"]]

        if not all_grades:  # To avoid ZeroDivisionError-->Check if there are any grades at all
            return 0  # Return 0 or handle the case where no grades are available

        return sum(all_grades) / len(all_grades)


if __name__ == '__main__':
    student_1 = Student("Ilichev Sergey Vladimirovich", "subjects")
    student_1.add_grade('Математика', 5)
    student_1.add_grade('Математика', 3)
    student_1.add_grade('Физика', 4)
    student_1.add_grade('Литература', 4)
    student_1.add_grade('Литература', 5)
    student_1.add_test_score('Литература', 95)
    student_1.add_test_score('Литература', 75)
    student_1.add_test_score('Математика', 75)
    print(student_1.get_average_test_score('Литература'))
    print(student_1.get_average_grade())


















