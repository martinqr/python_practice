'''
Exception Handling
'''

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print('You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')

'''
###########################################################################################################
###########################################################################################################
'''

'''
Packing and Unpacking Arguments in Python

We use two operators:

* for tuples
** for dictionaries


'''

'''
Unpacking Lists or tuple
'''

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
# print(one, middle, last)  

'''
Unpacking Dictionaries
'''

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
# print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

'''
Spreading in Python
'''
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
#print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
#print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']


''''
Enumerate
'''
for index, item in enumerate([20, 30, 40]):
    #print(index, item)
    '''
    0 20
    1 30
    2 40
    ''' 

# for index, i in enumerate(countries):
#     print('hi')
#     if i == 'Finland':
#         #print('The country {i} has been found at index {index}')
#         #The country Finland has been found at index 1.


'''
Zip
Sometimes we would like to combine 
lists when looping through them. See the example below:
'''


fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

# print(fruits_and_veges)


'''
Exercises:
'''

'''
Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
'''
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

*nordic_countries,es,ru = names

print(nordic_countries)
print(es)
print(ru)
