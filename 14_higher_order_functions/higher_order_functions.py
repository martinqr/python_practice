'''
Higher Order Functions
'''

'''
Function as a Parameter
'''

# def sum_numbers(nums):  # normal function
#     return sum(nums)    # a sad function abusing the built-in sum function :<

# def higher_order_function(f, lst):  # function as a parameter
#     summation = f(lst)
#     return summation
# result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
# print(result)       # 15

#######################################################################
#######################################################################


'''
Function as a Return Value
'''

def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

# result = higher_order_function('square')
# print(result(3))       # 9
# result = higher_order_function('cube')
# print(result(3))       # 27
# result = higher_order_function('absolute')
# print(result(-3))      # 3


##########################################################
##########################################################

'''
Python Decorators

'''

'''
Creating a decorator
'''


'''These decorator functions are higher order functions
that take functions as parameters'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
# print(greeting())   # WELCOME TO PYTHON


'''
Applying multiple decorator
'''

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
# print(greeting())   # ['WELCOME', 'TO', 'PYTHON']

##########################################################
##########################################################

'''
Built-in Higher Order Functions
'''

'''
Map ()

# syntax
map(function, iterable)

'''

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
# print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
# print(list(numbers_squared))    # [1, 4, 9, 16, 25]


'''
Filter ()

# syntax
filter(function, iterable)

'''

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
# print(list(even_numbers))       # [2, 4]


'''
Reduce ()
'''
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
# print(total)    # 15

##########################################################
##########################################################

'''
Exercises LEVEL 1
'''

# 3. Define a call function before map, filter or reduce, see examples.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map

def change_to_lower(name):
    lower = name.lower()
    return lower

my_new_lower = list(map(change_to_lower,names))
# print(my_new_lower)

# filter

def greater_than_five (num):
    if num > 5:
        return True
    return False

my_query = list(filter(greater_than_five,numbers))

# print(my_query)

# reduce

def multiply_next (num1,num2):
    return int(num1) * int(num2)

my_multiply = reduce(multiply_next,numbers)

# print(my_multiply)

# 4. Use for loop to print each country in the countries list.
# 5. Use for to print each name in the names list.
# 6. Use for to print each number in the numbers list.

def loop_everything (input):
    for input in input:
        print(input)

# loop_everything(countries)
# loop_everything(names)
# loop_everything(numbers)

'''
Exercises LEVEL 2
'''

# 1. Use map to create a new list by changing each country to uppercase in the countries list

def to_uppercase (list):
    uppercase = list.upper()
    return uppercase

my_new_list = list(map(to_uppercase,countries))

# print(my_new_list)

# 2. Use map to create a new list by changing each number to its square in the numbers list

def to_square(list):
    square = list ** 2
    return square

my_new_list = list(map(to_square,numbers))

# print(my_new_list)

# 3. Use map to change each name to uppercase in the names list

my_new_list = list(map(to_uppercase,names))

# print(my_new_list)

# 4. Use filter to filter out countries containing 'land'.

def containing_land (value):
    if 'land' in value:
        return True
    return False

my_new_list = list(filter(containing_land,countries))

# print(my_new_list)

# 5. Use filter to filter out countries having exactly six characters.

def containing_six_c (value):
    if len(value) == 6:
        return True
    return False

my_new_list = list(filter(containing_six_c,countries))

# print(my_new_list)

# 6. Use filter to filter out countries containing six letters and more in the country list.

def containing_six_c_or_more (value):
    if len(value) >= 6:
        return True
    return False

my_new_list = list(filter(containing_six_c_or_more,countries))

# print(my_new_list)

# 7. Use filter to filter out countries starting with an 'E'

def start_with_e (value):
    if value.startswith('E'):
        return True
    return False

my_new_list = list(filter(start_with_e,countries))

# print(my_new_list)

# 9. Declare a function called get_string_lists 
# which takes a list as a parameter and then returns a list containing only string items.

def get_string_lists (input_list):
    string_list = []
    for item in input_list:
        if type(item) == str:
            string_list.append(item)
    return string_list

my_list_1 = ['hola',2,'adios',22,32,1]

# print(get_string_lists(my_list_1))

# 10. Use reduce to sum all the numbers in the numbers list.

def sum_all (num1,num2):
    return num1 + num2

my_new_list = reduce(sum_all,numbers)
# print(my_new_list)

# 11. Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

def concatenate_countries(a,b):
    countries[-1] =  'and Iceland are north European countries'
    return f'{a},{b}'

my_countries_str = str(reduce(concatenate_countries,countries))

# print(my_countries_str)

# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the 
# countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

from my_countries import list_of_countries

contain_land = []
contain_ia = []
contain_island = []
contain_stan = []

def categorize_countries(my_input,input_list):
    for item in input_list:
        if my_input == contain_land and 'land' in item and item in input_list:
            contain_land.append(item)
        if my_input == contain_ia and 'ia' in item and item in input_list:
            contain_ia.append(item)
        if my_input == contain_island and 'island' in item and item in input_list:
            contain_island.append(item)
        if my_input == contain_stan and 'stand' in item and item in input_list:
            contain_stan.append(item)        
    return my_input


# print(categorize_countries(contain_land,list_of_countries))


'''
13. Create a function returning a dictionary, where keys stand for 
starting letters of countries and values are the number of country names starting with that letter.
'''

def country_name_count(countries):
  counts = {}
  for country in countries:
    first_letter = country[0]
    if first_letter in counts:
      counts[first_letter] += 1
    else:
      counts[first_letter] = 1
  return counts


# print(country_name_count(list_of_countries))


'''
14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
'''

def get_first_ten_countries (my_input):
    return my_input[0:10]


# print(get_first_ten_countries(list_of_countries))

'''
15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
'''

def get_last_ten_countries (my_input):
    return my_input[-11:-1]


# print(get_last_ten_countries(list_of_countries))

'''
Exercises LEVEL 3
'''

'''
1. Sort countries by name, by capital, by population
'''

from the_countries_data import countries_data

def sort_by_name(i):
    return i['name']

countries_data.sort(key=sort_by_name)

def sort_by_capital(i):
    return i['capital']

countries_data.sort(key=sort_by_capital)

def sort_by_population(i):
    return i['population']

countries_data.sort(key=sort_by_population)


'''
2. Sort out the ten most spoken languages by location.
'''

def most_spoken_languages (i):
    return i['languages']

countries_data.sort(key=most_spoken_languages)

# print(countries_data[0:10])

'''
3. Sort out the ten most populated countries.
'''

countries_data.sort(reverse =True ,key=sort_by_population)
# print(countries_data[0:10])