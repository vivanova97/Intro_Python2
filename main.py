'''
Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с
григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100,
а также если он кратен 400.
'''
from codecs import xmlcharrefreplace_errors
from ipaddress import summarize_address_range
from multiprocessing.sharedctypes import reduce_ctype
from operator import itemgetter, index
from os import lstat
from stringprep import in_table_a1
from symbol import if_stmt
from unicodedata import numeric

# year_input = int(input('Enter a year: '))
# if year_input % 4 == 0 and year_input % 100 != 0 or year_input % 400 == 0:
#     print('YES')
# else:
#     print('NO')

'''
Write a function that takes an integer n and returns a list of 
squares of numbers from 1 to n using the append() method.
'''

# n = int(input('Enter a number: '))
# list_of_squares = []
#
# for i in range(1, n + 1):
#     list_of_squares.append(i*i)
# print(list_of_squares)

'''
Problem 3: Insert an Element at a Specific Position
Write a function that takes a list, an element, and an index, then inserts the element at 
the specified index in the list using insert().
'''
# list_1 = [1,2,4,5]
# element_1 = int(input('Enter a number: '))
# index_1 = int(input('Enter an index: '))
#
# list_1.insert(index_1, element_1)
# print(list_1)

'''
Create a function that builds a list of even numbers from 1 to 20 but inserts them in reverse order
(e.g., 20, 18, 16, ...) using the insert() method.
'''
# list_1 = []
# for number in range(20,0,-2):
#     list_1.append(number)
#
# print(list_1)
#
# list_2 = []
# for number in range(2,21,2):
#     list_2.insert(0,number)
# print(list_2)

'''Write a function that takes a list and removes the last element using pop(). 
The function should return both the modified list and the popped element.'''

# list_1 = [1,2,3,4,5]
# print(f'{list_1.pop()}\n{list_1}')


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''
Write a function that takes a list and returns a new list that is the reverse 
of the original list using slicing.
'''
#
# list_1 = [1,2,3,4,5]
# list_1 = list_1[::-1]
#
# print(list_1)

'''Create a list of the squares of numbers from 1 to 10.
'''

# list_of_squares = [n**2 for n in range(1,11)]
# print(list_of_squares)

'''
Problem 2: Even Numbers
Task: Generate a list of all even numbers between 0 and 20.
'''

# even_numbers_1 = [n for n in range(0,21,2)]
# even_numbers_2 = [n for n in range(0,21) if n%2 ==0]
# print(even_numbers_1)
# print(even_numbers_2)

'''
Problem 3: Lengths of Strings
Task: Given a list of strings, create a new list that contains the lengths of each string.
'''

# words = ["apple", "banana", "cherry", "date"]
#
# length_of_string = [len(word) for word in words]
#
# print(length_of_string)
#
# words_length_combine = [(words[i], length_of_string[i]) for i in range(len(words))]
# print(words_length_combine)
#
# words_length_dict = {words[i]:length_of_string[i] for i in range(len(words))}
#
# print(words_length_dict)
#

'''
ask: Flatten the following list of lists into a single list.

'''

# nested_list = [[1, 2], [3, 4], [5, 6]]
#
# flattened_list = [item for listt in nested_list for item in listt]
# print(flattened_list)

'''
Given a string, create a list that contains only the vowels.
'''

# text = "List comprehensions are powerful!"
#
# list_1 = [letter for letter in text if letter in ['a','e','i','o','u']]
# print(list_1)

'''
Generate a list of squares for numbers between 1 and 15, but only include numbers that are divisible by 3.
'''

# list_of_squares = [i**2 for i in range(1,16) if i%3 == 0]
#
# print(list_of_squares)

'''
Given two lists, create a list of all possible pairs (as tuples).
'''

# list1 = [1, 2, 3]
# list2 = ['a', 'b']
#
# possible_pairs = [(a,b) for a in list1 for b in list2]
# print(possible_pairs)

'''
Given a list of integers, create a new list that contains each number squared, but only if the number is odd.
'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers_squared = [n**2 for n in numbers if n % 2 != 0]
# print(numbers_squared)

'''
Given a list of words, create a new list where each word is reversed.
'''

# words = ["hello", "world", "python"]
#
# reveresed_words = [word[::-1] for word in words]
# print(reveresed_words)

'''
Given a list of words, create a list containing the first letter of each word.
'''

# words = ["elephant", "tiger", "lion", "zebra"]
#
# first_letter = [word[0] for word in words ]
#
# print(first_letter)

'''
Given a 3x3 matrix (a list of lists), create a list containing the diagonal elements.
'''

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# diagonal_elements = [matrix[i][i] for i in range(len(matrix))]
# diagonal_elements1 = [matrix[-i][-i] for i in range(1,len(matrix)+1)]
#
# print(diagonal_elements)
# print(diagonal_elements1)

list_1 = [1,2,3,5,8,15,23,38]

# list_2 = [(num, num**2) for num in list_1 if num%2==0]
#
# print(list_2)

'''
1. Practice with map() and lambda
Problem: You have a list of temperatures in Celsius. 
Convert each temperature to Fahrenheit using the map() function and a lambda expression.

Hint: The formula to convert Celsius to Fahrenheit is F = C * 9/5 + 32
'''

# celsius_temps = [0, 12, 34, 100]
#
# fahrenheit_temps = list(map(lambda temp: temp * 9/5 + 32, celsius_temps))
#
# print(fahrenheit_temps)

'''
2. Practice with filter() and lambda
Problem: Given a list of integers, filter out all numbers that are not divisible by 3 
using the filter() function and a lambda expression.
'''
# numbers = [1, 3, 4, 6, 7, 9, 12, 14, 15]
#
# numbers_divisible_by_3 = list(filter(lambda number: number % 3 == 0, numbers))
#
# print(numbers_divisible_by_3)

'''
3. Practice with zip()
Problem: You have two lists: one with names and one with ages. 
Combine these lists into a single list of tuples using zip(), 
where each tuple contains a name and its corresponding age.
'''
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
#
# names_ages = list(zip(names, ages))
#
# print(*names_ages)

'''
4. Practice with enumerate()
Problem: Given a list of items, create a new list that contains tuples where 
the first element is the index of the item and the second element is the item itself. 
Use the enumerate() function.
'''

# items = ["apple", "banana", "cherry"]
#
# index_item = list(enumerate(items))
#
# print(index_item)

'''
5. Practice with sorted() and lambda
Problem: You have a list of dictionaries, where each dictionary represents a student 
with a name and a score. Sort the list of students by their scores in descending order 
using sorted() and a lambda expression.
'''
# students = [
#     {"name": "Alice", "score": 90},
#     {"name": "Bob", "score": 75},
#     {"name": "Charlie", "score": 85}
# ]
#
# students_sorted_by_score = list(sorted(students, key = lambda x: x['score'], reverse=True))
#
# print(students_sorted_by_score)

'''
7. Combining map(), filter(), and List Comprehension
Problem: You have a list of numbers. First, use filter() to keep only the odd numbers. 
Then, use map() to square each of the remaining numbers. Finally, use a list comprehension to 
filter out any squares that are greater than 50.
'''
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# odd_numbers_squared = list(map(lambda num: num ** 2, list(filter(lambda num: num % 2 != 0, numbers))))
# print(odd_numbers_squared)
#
# squares_less_than_50 = [num for num in odd_numbers_squared if num <= 50]
# print(squares_less_than_50)

'''
8. Practice with zip() and lambda
Problem: You have two lists: one with product names and another with their prices. 
Use zip() to combine them into a list of tuples, then sort the products by price in ascending order using sorted()
and a lambda expression.
'''

# products = ["apple", "banana", "cherry"]
# prices = [3.5, 2.0, 5.0]
#
# products_prices = list(sorted(list(zip(products, prices)), key= lambda selected_tup: selected_tup[1]))
#
# print(products_prices)

'''
9. Practice with enumerate() and List Comprehension
Problem: Given a list of strings, use enumerate() to create a new list where each element is a string 
that says "Index {index}: {item}". Use a list comprehension for this.
'''

# fruits = ["apple", "banana", "cherry"]
#
# index_fruit = {i:fruit for i, fruit in enumerate(fruits)}
#
# print(index_fruit)


'''
10. Practice with reduce() and lambda
Problem: Use the reduce() function to compute the product of all elements in a list. 
(Hint: Import reduce from functools.)
'''
# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
#
# numbers_product = reduce(lambda a, b: a * b, numbers)
#
# print(numbers_product)




