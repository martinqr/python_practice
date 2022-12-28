'''
Exercises: Level 1
'''

'''
1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
a) Read obama_speech.txt file and count number of lines and words 
b) Read michelle_obama_speech.txt file and count number of lines and words 
c) Read donald_speech.txt file and count number of lines and words 
d) Read melina_trump_speech.txt file and count number of lines and words
'''

# a,b,c,d)

def count_lines_words (path):
    with open(path,'r+') as my_file:
        count_words_read = my_file.read()
        count_words = len(count_words_read.split())
    print('Number of words =>',count_words)
    with open(path,'r+') as my_file:
        count_lines = len(my_file.readlines())
    print('Number of lines =>',count_lines)


# print('Obama Speech:')
# count_lines_words('E:\M_Code\python_practice/19_file_handling\obama_speech.txt')

# print('Michelle Speech:')
# count_lines_words('E:\M_Code\python_practice/19_file_handling\michelle_obama_speech.txt')

# print('Melina Speech:')
# count_lines_words('E:\M_Code\python_practice/19_file_handling\melina_trump_speech.txt')

# print('Donald Speech:')
# count_lines_words('E:\M_Code\python_practice/19_file_handling\donald_speech.txt')


'''
2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili'),
(4, 'Serbian')]

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]

'''

import json

from collections import Counter

# def most_spoken_languages (filename):
#     with open(filename,'r+',encoding='UTF-8') as my_file:
#         countries_list = json.load(my_file)
#         # lang_counter = Counter('languages')
#         my_languages = {}
# ¿       
        
#         # print(countries_dct.values())
#         # print(countries_dct[0])
#         # for i in countries_dct['name']:
#         #     print(i)


# most_spoken_languages('E:\M_Code\python_practice/19_file_handling\countries_data.json')


'''
Exercises: Level 2

Extract all incoming email addresses as a list from the email_exchange_big.txt file.
Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - 
a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

'''

def find_most_common_words (path,items):
    with open(path,'r+') as my_file:
        common_words_read = my_file.read().splitlines()
        common_words_str = ' '.join(common_words_read)
        common_words_list = common_words_str.split()
        common_words = Counter(common_words_list).most_common(items)
        print(common_words)


find_most_common_words('E:\M_Code\python_practice/19_file_handling\email_exchanges_big.txt',10)

