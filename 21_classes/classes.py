'''
Classes with methods
'''
class Person:
    def __init__(self,first_name = "T'challa" ,last_name = 'King',age = 36,country = 'Wakanda',city =  "Ro'ah"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city
        self.skills = []
    def person_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}'
    def add_skills(self,*skill):
        self.skills.append(skill)
        return f'{self.first_name} knows {self.skills}'

person_object = Person('John','Doe','30','Argentina','Bs.as')
person_object_default = Person()

'Person with new values =>', person_object.person_info()
# Person with new values => John Doe is 30 years old. He lives in Bs.as, Argentina
'Person default =>', person_object_default.person_info()
# Person default => T'challa King is 36 years old. He lives in Ro'ah, Wakanda

person_object_default_with_skills = Person()
person_object_default_with_skills.add_skills('Html','JavaScript')
# T'challa knows [('Html', 'JavaScript')]

'''
Inheritance

Allows us to define a class that inherits all the methods and properties from parent class
'''

class Student(Person):
    pass

new_student_1 = Student('Jose','Fernandez','20','Colombia','Bogota')
new_student_1.person_info()
# Jose Fernandez is 20 years old. He lives in Bogota, Colombia


'''
###########################################################################################################
###########################################################################################################
'''

'''
Exercises:
'''

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
from statistics import mean,median,mode,variance,stdev
import math
from collections import Counter

class Statistics:
    def __init__(self,data):
        self.data = data
    def count (self):
        return len(self.data)
    def sum (self):
        return sum(self.data)
    def min (self):
        return min(self.data)
    def range (self):
        return range(self.data)

    def mean (self):
        return round(mean(self.data))
    def median (self):
        return median(self.data)
    def mode (self):
        return mode(self.data)
    def std (self):
        return round(stdev(self.data),1)
    def var (self):
        return round(variance(self.data),1)
    def freq_dist (self):
        counts = Counter(self.data)
        return counts


data = Statistics(ages)

# print('Count:', data.count())
# print('Sum:', data.sum())
# print('Min: ', data.min())

# print('Mean: ', data.mean())
# print('Median: ', data.median())
# print('Mode: ', data.mode())
# print('Standard Deviation: ', data.std())
# print('Variance: ', data.var())
# print('Frequency Distribution: ', data.freq_dist())

'''
Create a class called PersonAccount. It has firstname, lastname, incomes, 
expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
Incomes is a set of incomes and its description. The same goes for expenses.
'''
class PersonAccount:
    def __init__(self,firstname,lastname,incomes,expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        total_income = {'total_income': sum((self.incomes.values()))}
        self.incomes.update(total_income)
        return self.incomes

    def total_expense(self):
        total_expense = {'total_expense': sum((self.expenses.values()))}
        self.expenses.update(total_expense)
        return self.expenses

    def account_info(self):
        return f'Name: {self.firstname} Lastname: {self.lastname}'
    
    def add_income(self,new_income):
        self.incomes.update(new_income)
        return self.incomes
    
    def add_expense(self,new_expense):
        self.expenses.update(new_expense)
        return self.expenses
    
    def account_balance(self):
        balance = self.incomes.get('total_income')
        expense = self.expenses.get('total_expense')
        return f'Current balance : Total income: {balance} Total expense: {expense}'
        


new_person = PersonAccount('John','Doe',{'main_job': 2000, 'freelance_job': 300, 'anothers_job': 100 },{'home': 100, 'misc': 50})

print(new_person.add_income({'store': 200}))
print(new_person.add_expense({'gas': 10}))
print(new_person.total_income())
print(new_person.total_expense())
print(new_person.account_balance())

