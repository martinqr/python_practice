
#1
# Get user input using input(“Enter your age: ”). If user is 18 or older, 
# give feedback: You are old enough to drive. If below 18 give feedback to wait 
# for the missing amount of years. Output:

#2
# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference 
# in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

#3
# Get two numbers from the user using input prompt. If a is greater than b return a is 
# greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

#4
# Write a code which gives grade to students according to theirs scores:

#5
# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: 
# September, October or November, the season is Autumn. December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

#6
# The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')

#7
# Here we have a person dictionary. Feel free to modify it!
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, 
# print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:

#1

# user_age = int(input('Enter your age: '))

# if user_age >= 18:
#     print('You are old enough to learn to drive.')
# else:
#     print('You need 3 more years to learn to drive.')

#2

# your_age = int(input('Enter your age: '))
# my_age = 30
# older_difference = int(your_age - my_age)
# younger_difference = int(my_age - your_age)

# if your_age == my_age:
#     print('We have the same age')
# elif your_age == 31:
#     print('You are 1 year older than me.')
# elif your_age == 29:
#     print('You are 1 year younger than me.')
# elif your_age > 30:
#     print(f'You are {older_difference} years older than me.')
# else:
#     print(f'You are {younger_difference} years younger than me.')

#3

# number_one = int(input('Enter number one: '))
# number_two = int(input('Enter number two: '))

# if number_one > number_two:
#     print(f'{number_one} is greater than {number_two}')
# elif number_two > number_one:
#     print(f'{number_two} is greater than {number_one}')
# else:
#     print('number one is equal to number two')

#4

# grade = int(input('Enter your score: '))

# if grade >=80 and grade <= 100:
#     print('A')
# elif grade >= 70 and grade <= 79:
#     print('B')
# elif grade >= 60 and grade <= 69:
#     print('C')
# elif grade >= 50 and grade <= 59:
#     print('D')
# else:
#     print('F')

#5

# my_season = input('Enter the month: ')
# my_season = my_season.lower()

# if my_season == 'september' or my_season == 'october' or my_season == 'november':
#     print('The season is Autumn')
# elif my_season == 'december' or my_season == 'january' or my_season == 'february':
#     print('The season is winter')
# elif my_season == 'march' or my_season == 'april' or my_season == 'may':
#     print('The season is Spring')
# elif my_season == 'june' or my_season == 'july' or my_season == 'august':
#     print('The season is Summer')
# else:
#     print('Incorrect data')

#6

# fruits = ['banana', 'orange', 'mango', 'lemon']

# my_fruit= input('Enter a fruit: ')
# my_fruit = my_fruit.lower()

# if my_fruit in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(my_fruit)
#     print(fruits)

#7

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}

#7.1
#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

# if 'skills' in person.keys():
#     print(person['skills'][int(len(person['skills']) / 2)])
# else:
#     print('We dont have person skills')

#7.2
#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

# my_skills = person['skills']
# index_python = my_skills.index('Python')

# if 'skills' in person.keys():
#     if 'Python' in person['skills']:
#         print(f'Found Python in index {index_python}')
# else:
#     print('We dont have person skills')

#7.3

# If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!

# if 'skills' in person.keys():
#         if person['skills'] == ['JavaScript','React'] or person['skills'] == ['React','JavaScript'] :
#                 print('He is a front end developer')
#         if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
#                 print('He is a backend developer')
#         if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
#                 print('He is a fullstack developer')
# else:
#     print('unknown title')

#7.4

#  If the person is married and if he lives in Finland, print the information in the following format:
#      Asabeneh Yetayeh lives in Finland. He is married.

# your_name = input('Enter your name: ')
# your_status = input('Are you married ?: ')
# your_location = input('Enter your location: ')

# your_status = your_status.lower()
# your_location = your_location.lower()

# if your_status == 'yes' and your_location == 'finland':
#     print(f'{your_name} lives in Finland. He is married')
# else:
#     print(f'{your_name} lives in {your_location}. He is not married')








