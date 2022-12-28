'''
Opening Files for Reading
'''


txt_file = open('python_practice/19_file_handling/my_file.txt', 'r+') # reading and writing the file

# print(txt_file.read()) # read the whole text as string

# read(10) print the first 10 characters of the text file.

# readline(): read only the first line

# readlines()read all the text line by line and returns a list of lines ['Argentina\n', 'Colombia\n', 'Mexico']

# txt_file.read().splitlines() Another way to get all the lines as a list is using splitlines():  ['Argentina', 'Colombia', 'Mexico']

'''
Opening Files for Writing and Updating
'''

# with open('python_practice/19_file_handling/my_file.txt', 'a') as txt_file_2:
#     txt_file_2.write('\nPeru')

'''
"a" - append - will append to the end of the file, if the file does not it creates a new file.
"w" - write - will overwrite any existing content, if the file does not exist it creates.
'''

# Argentina
# Colombia
# Mexico
# Peru

#####################################################

# with open('python_practice/19_file_handling/my_teams.txt', 'w') as txt_file_3:
#     txt_file_3.write('Barcelona \nReal Madrid')

# Barcelona
# Real Madrid

'''
Deleting Files
'''

import os

# os.remove('python_practice/19_file_handling/my_teams.txt')

# If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:

# if os.path.exists('python_practice/19_file_handling/my_teams.txt'):
#     os.remove('python_practice/19_file_handling/my_teams.txt')
# else:
#     print('The file does not exist')

#####################################################

'''
File with json Extension
'''
import json

'''
Changing JSON to a Dictionary
'''

person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''

person_dct = json.loads(person_json)
# print(person_dct)

'''
Changing Dictionary to JSON
'''
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}

person_json = json.dumps(person,indent=2) # indent could be 2, 4, 8. It beautifies the json
print(person_json[0])

'''
Saving as JSON File
'''

# with open('python_practice/19_file_handling/my_person.json', 'w', encoding='utf-8') as to_json:
#     json.dump(person,to_json,ensure_ascii=False,indent=2)


'''
File with csv Extension
'''
import csv

with open('E:\M_Code\python_practice/19_file_handling\data.csv','r') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
        iterable = zip(header,row)
        country_dict = {key: value for key,value in iterable}
        data.append(country_dict)

data_indent = json.dumps(data[0],indent=4)
# print(data_indent)

'''
{
    "Rank": "36",
    "CCA3": "AFG",
    "Country/Territory": "Afghanistan",
    "Capital": "Kabul",
    "Continent": "Asia",
    "2022 Population": "41128771",     
    "2020 Population": "38972230",     
    "2015 Population": "33753499",     
    "2010 Population": "28189672",     
    "2000 Population": "19542982",     
    "1990 Population": "10694796",     
    "1980 Population": "12486631",
    "1970 Population": "10752971",
    "Area (km\u00c2\u00b2)": "652230",
    "Density (per km\u00c2\u00b2)": "63.0587",
    "Growth Rate": "1.0257",
    "World Population Percentage": "0.52"
}
'''


#####################################################################
#####################################################################
#####################################################################