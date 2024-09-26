"""Homework for 7th Seminar"""

__all__ = ['group_file_rename', 'delete_old_files', 'find_files_with_extension']

import os
import time
from pathlib import Path
import shutil


"""
Задание 1. Функцию группового переименования файлов.
Напишите функцию группового переименования файлов. Она должна:
1. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
2. принимать параметр количество цифр в порядковом номере.
3. принимать параметр расширение исходного файла. Переименование
должно работать только для этих файлов внутри каталога.
4. принимать параметр расширение конечного файла.
5. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя,
если оно передано. Далее счётчик файлов и расширение.
"""

def group_file_rename(folder_path: str, serial_number_len: int, original_file_extension: str,
                      original_name_part: tuple[int,int]=None, new_name: str='', new_file_extension: str=None):
    """Renaming files in given folder

    :param folder_path: path to catalog with files
    :param serial_number_len: length of serial number
    :param original_file_extension: original file extension
    :param original_name_part: part of original name you want to save (start, finish)
    :param new_name: final name of file
    :param new_file_extension: new file extension if you want to change extension or 'None'
    """
    if not Path(folder_path).is_dir():
        raise FileNotFoundError(f"{folder_path} not found.")

    if original_name_part is None:
       original_name_part = (0,0)
       start_org_name, end_org_name = original_name_part
    else:
        start_org_name, end_org_name = original_name_part
        start_org_name, end_org_name = start_org_name-1, end_org_name

    if new_file_extension is None:
        new_file_extension = original_file_extension

    folder = Path(folder_path)

    for file_num, obj in enumerate(folder.iterdir(), start=1):
        if obj.is_file() and obj.suffix == f'.{original_file_extension}':
            original_name = obj.stem[start_org_name:end_org_name]
            new_filename = f'{original_name}{new_name}{str(file_num).zfill(serial_number_len)}.{new_file_extension}'
            obj.rename(folder/ new_filename)


"""
Задача 2. Создание архива каталога
Напишите скрипт, который создает архив каталога в формате .zip. 
Скрипт должен принимать путь к исходному каталогу и путь к целевому архиву. 
Архив должен включать все файлы и подпапки исходного каталога.
easier to just use shutil:

# Specify the absolute path to the folder you want to archive
folder_to_archive = '/path/to/your/folder'

# Create the zip archive
shutil.make_archive('/path/to/save/your_archive', 'zip', folder_to_archive)
"""

"""
Задача 3. Удаление старых файлов
Напишите скрипт, который удаляет файлы в указанном каталоге, которые не изменялись более заданного количества дней. 
Скрипт должен принимать путь к каталогу и количество дней.
"""
def delete_old_files(directory_path: str, num_of_days: int):
    """Deletes files older than specified number_of_days

    :param directory_path: Path to directory containing files.
    :param num_of_days: Takes in max number of days since last modification on file.
    """
    num_of_days_in_seconds = num_of_days * 86400

    for path, folders, files in os.walk(directory_path):
        for file in files:
            if time.time() - os.path.getmtime(os.path.join(path, file)) > num_of_days_in_seconds:
                os.remove(os.path.join(path, file))


def delete_old_files_gpt(directory_path: str, num_of_days: int):
    """
    Deletes files from the directory that have not been modified in the given number of days.

    Args:
    directory_path (str): The directory to search for files.
    num_of_days (int): The number of days to check for file modification times.
    """
    num_of_days_in_seconds = num_of_days * 86400  # Convert days to seconds
    current_time = time.time()

    # Use Pathlib to iterate through files in the directory
    directory = Path(directory_path)

    # Walk through directory and remove old files
    for file_path in directory.rglob('*'):  # Recursively go through all files, better version to go through all files
        if file_path.is_file():
            file_mod_time = file_path.stat().st_mtime  # Get the last modified time
            if current_time - file_mod_time > num_of_days_in_seconds:
                try:
                    print(f'Deleting {file_path}')  # Print confirmation before deletion
                    file_path.unlink()  # Remove the file
                except Exception as e:
                    print(f'Error deleting {file_path}: {e}')  # Handle possible errors


"""
Задача 4. Поиск файлов по расширению
Напишите функцию, которая находит и перечисляет все файлы с заданным расширением в указанном каталоге и 
всех его подкаталогах. Функция должна принимать путь к каталогу и расширение файла.
"""

def find_files_with_extension(folder_path: str, extension: str) -> None:
    """Finds files within the given folder with the extension given as a parameter

    :param folder_path: Path to folder where the files lie
    :param extension: Intended extension
    """
    if not Path(folder_path).is_dir():
            raise FileNotFoundError(f"{folder_path} not found.")

    for file_path in Path(folder_path).rglob('*'):
        if file_path.is_file() and file_path.suffix == '.txt':
            print(file_path.name)



if __name__ == '__main__':
    # os.chdir('sample_files')
    # group_file_rename(folder_path='/Users/valeriaivanova/PycharmProjects/testPythonProject/seminar_7/sample_files', serial_number_len=3, original_file_extension='txt',
    #                   original_name_part =(1,3), new_name='ample')
    # delete_old_files('/Users/valeriaivanova/PycharmProjects/testPythonProject/seminar_7', 3)
    # find_files_with_extension(folder_path='/Users/valeriaivanova/PycharmProjects/testPythonProject/seminar_7/', extension='txt')