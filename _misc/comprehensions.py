
'''
Comprehensions
'''
import random,zipfile
from random import randint

my_list = [element for element in range(1,11) if element < 5]
# [1, 2, 3, 4]

my_dict = {}

for i in range(1,5):
    my_dict[i] = i * 2
#{1: 2, 2: 4, 3: 6, 4: 8}

my_dict_2 = {i: i*2 for i in range(1,5)}

print(my_dict_2)
#{1: 2, 2: 4, 3: 6, 4: 8}

countries = {'col','arg','mex'}

population_v2 = {country: random.randint(1,100) for country in countries}
# {'mex': 44, 'arg': 14, 'col': 22}


# names = ['nico','zule','santi']
# ages = [12,56,98]

# # print(list(zip(names,ages)))

# new_dict = {name: age for (name,age) in zip(names,ages)}
# print(new_dict)

# result = {country:population for (country,population) in population_v2.items() if population > 20}
# # {'mex': 44, 'col': 22}

txt = 'hola soy martin'

unique = {c: c.upper() for c in txt if c in 'aeiou'}

print(unique)