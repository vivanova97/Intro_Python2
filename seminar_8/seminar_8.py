import csv
import json
import pickle
from imghdr import test_pbm
from pathlib import Path

""""
📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
📌 Имена пишите с большой буквы.
📌 Каждую пару сохраняйте с новой строки.
"""
def txt_file_to_json():
    with (
        open('../seminar_7/practice.txt', mode='r', encoding='utf-8') as txt_f,
        open('new_file.json', mode='w', encoding='utf-8') as json_f
    ):
        txt_file_dict = dict()

        for line in txt_f:
            key, value = line.strip('\n').split('|')
            txt_file_dict[key] = value

        json.dump(txt_file_dict, json_f, ensure_ascii=False, indent=2)

"""
📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
📌 После каждого ввода добавляйте новую информацию в JSON файл.
📌 Пользователи группируются по уровню доступа.
📌 Идентификатор пользователя выступает ключём для имени.
📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
📌 При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
def add_to_json_file():

    json_dict = dict()
    while True:
        name = input('Please enter your name: ')
        id_ = input('Please enter your id: ')
        level = int(input('Please enter level of authentication: '))

        if level not in json_dict:
            json_dict[level] = {}

        json_dict[level][id_] = name

        with open('name_level_id.json', mode='w', encoding='utf-8') as json_f:
            json.dump(json_dict, json_f, ensure_ascii=False, indent=2)


"""📌 Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV."""
def save_json_to_csv():
    with (
        open('name_level_id.json', mode='r', encoding='utf-8') as json_f,
        open('name_level_id.csv', mode='w', newline='', encoding='utf-8') as csv_f
    ):
        json_dict = json.load(json_f)
        csv_write = csv.DictWriter(csv_f, fieldnames=['level','id','name'])

        csv_write.writeheader()

        for level, dict_ in json_dict.items():
            for id_, name in dict_.items():
                dict_for_csv = dict()
                dict_for_csv["level"] = level
                dict_for_csv["id"] = id_
                dict_for_csv["name"] = name
                csv_write.writerow(dict_for_csv)


def csv_to_json_using_csv_reader(csv_file_path: str, json_file_path: str):
    """
    📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
    📌 Дополните id до 10 цифр незначащими нулями.
    📌 Добавьте поле хеш на основе имени и идентификатора.
    📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
    📌 Имя исходного и конечного файлов передавайте как аргументы функции.

    :param csv_file_path: path to csv_file
    :parm json_file_path: path to csv_file
    """

    with (
        open(csv_file_path, mode='r', encoding='utf-8', newline='') as csv_f,
        open(json_file_path, mode='w', encoding='utf-8') as json_f
    ):
        csv_read = csv.reader(csv_f)
        json_list = []
        headers = next(csv_read)

        for index, line in enumerate(csv_read):
            json_dict = dict(zip(headers,line))
            json_dict['id'] = str(json_dict['id']).zfill(10)
            json_dict['hash'] = hash(f'{json_dict['name']}{json_dict['id']}')
            json_list.append(json_dict)

        json.dump(json_list, json_f, ensure_ascii=False, indent=2)


csv_to_json_using_csv_reader(csv_file_path='name_level_id.csv', json_file_path='name_level_id_2.json')

"""📌 Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых 
pickle файлов."""

def convert_all_json_to_pickle(directory_path: str):
    for i, path in enumerate(Path(directory_path).rglob('*.json'),1):
        with (
            open(path, mode='r', encoding='utf-8') as json_f,
            open(f'new_file{i}.pickle', mode='wb') as pickle_f
        ):
           temp_dict = json.load(json_f)
           pickle.dump(temp_dict,pickle_f)


"""
Задание No6
📌 Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""
def convert_pickle_to_csv(pickle_file_path: str, csv_file_path: str):

    with (
        open(f'{pickle_file_path}', mode='rb') as pickle_f,
        open(f'{csv_file_path}', mode='w', encoding='utf-8', newline='') as csv_f
    ):
        pickle_file_list = pickle.load(pickle_f)
        csv_write = csv.DictWriter(csv_f, fieldnames=[key for key in pickle_file_list[0].keys()],
                                   quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        for dictionary in pickle_file_list:
            csv_write.writerow(dictionary)


"""
Задание No7
📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
📌 Распечатайте его как pickle строку.
"""
def csv_to_pickle(csv_file_path: str):
    with open(f'{csv_file_path}', mode='r', encoding='utf-8', newline='') as csv_f:
        csv_read = csv.reader(csv_f, quoting=csv.QUOTE_NONNUMERIC)
        csv_as_pickle_str = pickle.dumps([line for line in csv_read])
        print(csv_as_pickle_str)


if __name__ == '__main__':
    pass
    # convert_all_json_to_pickle(f'{Path().cwd()}')
    # convert_pickle_to_csv('new_file1.pickle', 'new_file1.csv')
    # csv_to_pickle('new_file1.csv')
    # txt_file_to_json()
    # add_to_json_file()
    # save_json_to_csv()
    # csv_to_json_using_csv_reader(csv_file_path='name_level_id.csv', json_file_path='name_level_id_2.json')
    # with open('new_file.json', mode='r', encoding='utf-8') as json_f:
    #     new_dict = json.load(json_f) # turning json object into python object
    #     new_str = json.dumps(new_dict) # turning python object into json string object
    #     print(new_dict)
    #     print(new_str)