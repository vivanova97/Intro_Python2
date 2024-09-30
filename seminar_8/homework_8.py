import csv
import json
import pickle
from pathlib import Path
import os




def directory_info_json_csv_pickle(directory_path: str, json_path: str, csv_path: str, pickle_path: str):
    """
    Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
    Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
    Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий размер
    файлов в ней с учётом всех вложенных файлов и директорий. Соберите из созданных на уроке и в рамках домашнего задания
    функций пакет для работы с файлами разных форматов.

    :param directory_path: Directory path which contains objects which you want to get information on.
    :param json_path: Path to json file where you want to write the information to.
    :param csv_path: Path to csv file where you want to write the information to.
    :param pickle_path: Path to pickle file where you want to write the information to.
    """

    directories_list = []

    for obj in Path().rglob('*'):
        directory_dict = dict()
        directory_dict['object'] = obj.name
        directory_dict['parent directory'] = obj.parent.absolute().name
        directory_dict['file'] = True if obj.is_file() else False
        directory_dict['directory'] = True if obj.is_dir() else False
        directory_dict['size'] = obj.stat().st_size if obj.is_file() else sum(i.stat().st_size for i in obj.glob('*'))
        directories_list.append(directory_dict)

    with(
        open(f'{json_path}', mode='w', encoding='utf-8') as json_f,
        open(f'{csv_path}', mode='w', encoding='utf-8', newline='') as csv_f,
        open(f'{pickle_path}', mode='wb') as pickle_f
    ):
        json.dump(directories_list, json_f, ensure_ascii=False, indent=2)
        pickle.dump(directories_list, pickle_f)
        csv_write = csv.DictWriter(csv_f, fieldnames=[key for key in directories_list[0]])
        csv_write.writeheader()
        csv_write.writerows(directories_list)


def combine_json_files(files: list, combined_file: str):
    """
    Задача 2. Объединение данных из нескольких JSON файлов
    Напишите скрипт, который объединяет данные из нескольких JSON файлов в один.
    Каждый файл содержит список словарей, описывающих сотрудников компании (имя, фамилия, возраст, должность).
    Итоговый JSON файл должен содержать объединённые списки сотрудников из всех файлов.

    :param files: List of all files that you want to merge.
    :param combined_file: Path where you want to save the combined file.
    """

    combined_list = []
    for file in files:
        try:
            with open(file, mode='r', encoding='utf-8') as f:
                file_list = json.load(f)
                combined_list.extend(file_list)
        except json.JSONDecodeError:
            print(f'Error in reading JSON file: {file}')
    with open(combined_file, mode='w', encoding='utf-8') as combined_f:
        json.dump(combined_list, combined_f,ensure_ascii=False,indent=2)


def json_to_csv(json_path: str, csv_path: str):
    """Задача 3. Агрегирование данных из CSV файла
    Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV файл.
    JSON файл содержит данные о продуктах (название, цена, количество на складе).
    В CSV файле каждая строка должна соответствовать одному продукту.

    :param json_path: Path to json_file that we want to read and convert to csv.
    :parm csv_path: Path to csv_file into which we want to write json_file data."""
    try:
        with(
            open(json_path, mode='r', encoding='utf-8') as json_f,
            open(csv_path, mode='w', encoding='utf-8', newline='') as csv_f
        ):
                json_list = json.load(json_f)
                if not isinstance(json_list, list) or not all(isinstance(item, dict) for item in json_list):
                    raise ValueError("Incorrect data format in JSON file.")

                csv_write = csv.DictWriter(csv_f, fieldnames=[key for key in json_list[0].keys()], quoting=csv.QUOTE_NONNUMERIC)
                csv_write.writeheader()
                for product in json_list:
                    csv_write.writerow(product)

    except json.JSONDecodeError:
        print(f'Error in reading JSON file: {json_path}')


"""Задача 4. Агрегирование данных из CSV файла
Напишите скрипт, который считывает данные из CSV файла, содержащего информацию о продажах (название продукта,
количество, цена за единицу), и подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в 
новом CSV файле. Пример: Из файла sales.csv нужно создать файл total_sales.csv, где для каждого продукта будет 
указана общая выручка."""

def aggregate_data_from_csv(original_csv: str, new_csv: str):
    with(
        open(original_csv, mode='r', encoding='utf-8', newline='') as csv_1,
        open(new_csv, mode='w', encoding='utf-8', newline='') as csv_2
    ):
        csv_read = csv.DictReader(csv_1)
        fieldnames = csv_read.fieldnames
        csv_write = csv.DictWriter(csv_2, fieldnames= fieldnames, quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        aggregated_data = {}

        for sale in csv_read:
            product = sale['product']
            quantity = int(sale['quantity'])
            price = float(sale['price'])

            if product not in aggregated_data:
                aggregated_data[product] = {'quantity': 0, 'price': 0}

            # Aggregate the quantities and prices
            aggregated_data[product]['quantity'] += quantity
            aggregated_data[product]['price'] += price

        # Write the aggregated data to the new CSV
        for product, data in aggregated_data.items():
            csv_write.writerow({'product': product, 'quantity': data['quantity'], 'price': data['price']})


"""
Задача 5. Конвертация CSV в JSON с изменением структуры данных
Напишите скрипт, который считывает данные из CSV файла и сохраняет их в JSON файл с другой структурой. 
CSV файл содержит данные о книгах (название, автор, год издания). В JSON файле данные должны быть сгруппированы по 
авторам, а книги каждого автора должны быть записаны как список.
Пример: Из файла books.csv нужно создать файл books_by_author.json, где книги сгруппированы по авторам.
"""

if __name__ == '__main__':
    aggregate_data_from_csv('/Users/valeriaivanova/Downloads/Module8/zad_4/sales.csv',
                            f'{Path().cwd() / 'total_sales.csv'}')

    # directory_info_json_csv_pickle(directory_path=f'{Path().cwd()}', json_path=f'{Path().cwd() / 'directory_info.json'}',
    #                                csv_path=f'{Path().cwd() / 'directory_info.csv'}',
    #                                pickle_path=f'{Path().cwd() / 'directory_info.pickle'}')

    # json_files_path = Path('/Users/valeriaivanova/downloads/module8/zad_2/')
    # json_files_list = [file for file in json_files_path.glob('*.json')]
    # combine_json_files(json_files_list,
    #                    f'{Path().cwd()/'combined_json_file.json'}')
    # json_to_csv('/Users/valeriaivanova/downloads/module8/zad_3/products.json',
    #             f"{Path().cwd() / 'products.csv'}")



