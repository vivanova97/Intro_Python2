import random
import string

'''
✔ Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
'''
list_1 = ['cat', 'dog', 1, 2, 3, 2, 3, 3, 3, 'turtle', 'cat', 'cat']

def return_duplicates(list_with_duplicates: list) -> list:
    list_of_duplicates = list(set([i for i in list_with_duplicates if list_with_duplicates.count(i) > 1]))
    # duplicates_list2 = list(set(filter(lambda i: list_1.count(i) > 1, list_1))) # additional version using filter()
    return list_of_duplicates

# print(return_duplicates(list_1))

'''
✔ В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку.
'''
def ten_most_common_words(text: str, number_of_words: int = 10) -> dict:
    text = text.lower()
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for char in text:
        if char in punc:
            text = text.replace(char, '')

    words_list = text.split()
    word_count_dict = dict()

    for word in words_list:
        if word not in word_count_dict:
            word_count_dict[word] = words_list.count(word)

    sorted_by_count = dict(sorted(word_count_dict.items(), key=lambda tup: tup[1], reverse=True)[:number_of_words])

    print(sorted_by_count)


sample_text = ''' We, the 'Publisher', and a select group of trusted partners (843), known as 'Vendors', 
                  need your consent for data-processing purposes. These purposes include to store and/or access 
                  information on a device, like cookie management and to process personal data such as standard 
                  information sent by a device and other unique identifiers for personalised ads and content, 
                  ad and content measurement, audience insights and product development. With your consent we 
                  and our partners may use precise geolocation data and actively scan device characteristics for
                  identification. You may consent to the processing described above or access more detailed 
                  information and customise your choices. The given consent will apply to this site only. 
                  Please take into consideration that some of your personal data processing may rely on legitimate 
                  interest which does not require your consent but you have a right to object to this.
'''

# ten_most_common_words(sample_text, 10)


'''
✔ Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
✔ *Верните все возможные варианты комплектации рюкзака.
'''
my_camping_gear = {
    "Палатка": 2.5,
    "Спальный мешок": 1.2,
    "Коврик для сна": 0.8,
    "Фонарик": 0.3,
    "Еда": 2.0,
    "Вода (1 литр)": 1.0,
    "Одежда": 1.1,
    "Аптечка": 0.5,
    "Нож": 0.2
}

def all_backpack_variations(camping_gear: dict, max_backpack_capacity: float = 4) -> list[set]:

    all_possible_variations = []

    for item, weight in camping_gear.items():
        weight_sum = weight
        possible_variation = {item}
        for item_, weight_ in camping_gear.items():
            if item == item_:
                continue
            elif weight_sum + weight_ <= max_backpack_capacity:
                weight_sum += weight_
                possible_variation.add(item_)
        if possible_variation not in all_possible_variations:
            all_possible_variations.append(possible_variation)

    return all_possible_variations

# print(*all_backpack_variations(my_camping_gear), sep='\n')


'''
Поиск наибольшего числа в списке
Напишите программу, которая принимает список чисел через строку и возвращает наибольшее число в этом списке.
'''
def find_max_num():
    num_list = input('Enter a list of nums, separate each number with a space: ').split()
    max_num = num_list[0]

    for num in num_list:
        if num > max_num:
            max_num = num

    return max_num

# print(find_max_num())

'''
Напишите программу, которая принимает строку и определяет, является ли она палиндромом (читается одинаково с обеих сторон).
'''
def check_if_palindrome(word: str) -> bool:
    word = word.lower()
    return word == word[::-1]

# print(check_if_palindrome('racecar'))

'''
Напишите программу, которая генерирует случайный пароль заданной длины, состоящий из букв, цифр и специальных символов.
'''
def generate_password(length: int = 10) -> str:
    password = random.choices(string.printable, k=length)
    return ''.join(password)

# print(generate_password(8))

'''
Напишите программу, которая принимает два слова и определяет, являются ли они анаграммами.
'''
def anagram_check1(word_1: str, word_2: str) -> bool: # version 1
    word_1 = word_1.replace(' ', '').lower()
    word_2 = word_2.replace(' ', '').lower()
    word_1_letter_count = {letter:word_1.count(letter) for letter in word_1}
    word_2_letter_count = {letter:word_2.count(letter) for letter in word_2}
    # if len(word_1) != len(word_2) or word_:
    if word_1_letter_count == word_2_letter_count:
        return True
    return False

# print(anagram_check1('William Shakespeare', 'I am a weakish speller'))


def anagram_check2(word_1: str, word_2: str) -> bool: # version 2
    # Убираем пробелы и приводим к нижнему регистру
    word_1 = word_1.replace(' ', '').lower()
    word_2 = word_2.replace(' ', '').lower()

    # Если длины строк разные, они не могут быть анаграммами
    if len(word_1) != len(word_2):
        return False

    # Используем сортировку: анаграммы будут одинаковы при сортировке
    return sorted(word_1) == sorted(word_2)

# print(anagram_check2('William Shakespeare', 'I am a weakish speller'))