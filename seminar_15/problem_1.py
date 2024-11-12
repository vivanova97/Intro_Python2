"""Задание No1
📌 Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль.
"""
import logging

FORMAT = '{levelname:<8} - {asctime}. In module "{name}" ' \
         'in line {lineno:03d} function"{funcName}()" at {created} seconds: {msg}'
logging.basicConfig(filename='seminar_15.log', encoding='utf-8', level=logging.ERROR, format= FORMAT, style='{')
logger = logging.getLogger(__name__)

try:
    10/0
except Exception as e:
    logger.error(f"ZeroDivisionError, {e}")
