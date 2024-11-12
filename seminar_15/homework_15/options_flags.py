"""Задача 4. Опции и флаги
Напишите скрипт, который принимает два аргумента командной строки: число и строку. Добавьте следующие опции:
● --verbose, если этот флаг установлен, скрипт должен выводить дополнительную информацию о процессе.
● --repeat, если этот параметр установлен, он должен указывать, сколько раз повторить строку в выводе."""

import argparse


def main():
    # Creates parser
    parser = argparse.ArgumentParser(description='Processing number and string with extra options')

    # Adds required arguments
    parser.add_argument('text', type=str, help='text for output')
    parser.add_argument('number', type=int, help='int for output')

    # Adds optional arguments
    parser.add_argument('--verbose', action='store_true', help='returns extra information')
    parser.add_argument('--repeat', type=int, default=1, help='repeats a number of times')

    # Parses arguments
    args = parser.parse_args()

    # Checks if --verbose is true
    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, text="{args.text}", repeat={args.repeat}')

    # Prints number and text according to number specified in repeat
    print(f'Число: {args.number}, Строка: {args.text * args.repeat}')


if __name__ == '__main__':
    main()

