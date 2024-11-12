"""Задача 5. Запуск из командной строки
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов
namedtuple. Каждый объект хранит: имя файла без расширения или название каталога, расширение, если это файл,
флаг каталога, название родительского каталога. В процессе сбора сохраните данные в текстовый файл используя
логирование."""

import argparse
from collections import namedtuple
from pathlib import Path
import logging

def main():
    # Created parser and added arguments
    parser = argparse.ArgumentParser('file path info')
    parser.add_argument('path', type=Path, help='full Path object')
    arg = parser.parse_args()

    # Created Path object using path argument passed in terminal
    arg = Path(arg.path)

    # Created namedtuple object and instance
    path_class = namedtuple('path', ['file_or_catalog_name', 'extension', 'file_bool', 'catalog_bool',
                               'parent_catalog'])

    path_instance = path_class(arg.stem, arg.suffix, arg.is_file(), arg.is_dir(), arg.parent.name)

    # Created logger, set formatter, added file handler
    logger = logging.getLogger('path info logger')
    logger.setLevel(level=logging.INFO)
    file_handler = logging.FileHandler('path_info.log', mode='a', encoding='utf-8')
    formatter = logging.Formatter('{asctime} - {msg}', style='{')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Wrote to log file
    logger.info(f"name:{path_instance.file_or_catalog_name}, extension: {path_instance.extension}, "
                f"file: {path_instance.file_bool}, catalog: {path_instance.catalog_bool}, "
                f"parent_catalog: {path_instance.parent_catalog}")



