# Exercises: Day 8

#1 Create an empty dictionary called dog
#2 Add name, color, breed, legs, age to the dog dictionary
#3 Create a student dictionary and add first_name, last_name, 
# gender, age, marital status, skills, country, city and address as keys for the dictionary
#4 Get the length of the student dictionary
#5 Get the value of skills and check the data type, it should be a list
#6 Modify the skills values by adding one or two skills
#7 Get the dictionary keys as a list
#8 Get the dictionary values as a list
#9 Change the dictionary to a list of tuples using items() method
#10 Delete one of the items in the dictionary
#11 Delete one of the dictionaries


#1

dog = dict()

#2

dog = {
    'Name': 'Hachi',
    'Color': 'Black',
    'Breed': 'None',
    'Legs': 4,
    'Age': 6
}

#3

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': '30',
    'marital': 'Single',
    'skills': ['Html','CSS','Python'],
    'country': 'Argentina',
    'city': 'Buenos aires',
    'address': {
        'street':'False street',
        'zipcode':'0220'
    }
}

#4

len(student)

#5

type(student['skills'])

#6

student['skills'].extend(('React','JavaScript')) #Add items

#7

student.keys()

#8

student.values()

#9

student.items()

#10

student.pop('address')

#11

del dog







