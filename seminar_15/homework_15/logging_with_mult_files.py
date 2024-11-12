"""Задание 1. Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы. Логи уровня DEBUG и INFO должны сохраняться в
debug_info.log, а логи уровня WARNING и выше — в warnings_errors.log.
"""

import logging

# Created logger and formatter
logger = logging.getLogger('logging_with_mult_files')
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('{asctime} - {levelname} - {msg}', style='{')

# Added debug and info level file handler to logger and set formatter
debug_info_handler = logging.FileHandler('debug_info.log', encoding='utf-8')
debug_info_handler.setLevel(level=logging.DEBUG)
debug_info_handler.setFormatter(formatter)
logger.addHandler(debug_info_handler)

# Added warning and errors handler to logger and set formatter
warning_errors_handler = logging.FileHandler('warnings_errors.log', encoding='utf-8')
warning_errors_handler.setLevel(level=logging.WARNING)
warning_errors_handler.setFormatter(formatter)
logger.addHandler(warning_errors_handler)

# Tested adding logs to files
logger.debug('Debug level message.')
logger.info('Info level message.')
logger.error('Error!')
logger.warning('Warning!')
logger.critical('Critical.')

