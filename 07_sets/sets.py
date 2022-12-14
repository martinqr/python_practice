

# sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Exercises: Level 1

#1 Find the length of the set it_companies
#2 Add 'Twitter' to it_companies
#3 Insert multiple IT companies at once to the set it_companies
#4 Remove one of the companies from the set it_companies
#5 What is the difference between remove and discard

# Exercises: Level 2

#6 Join A and B
#7 Find A intersection B
#8 Is A subset of B
#9 Are A and B disjoint sets
#10 Join A with B and B with A
#11 What is the symmetric difference between A and B
#12 Delete the sets completely

# Exercises: Level 3

#13 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
#14 Explain the difference between the following data types: string, list, tuple and set
#15 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

#1

len(it_companies)

#2

it_companies.add('Twitter')

#3

it_companies.update({'Tesla','Space X'})

#4

it_companies.remove('Tesla')

#5

# What is the difference between remove and discard
# remove : eliminate a item give a if is not in the set throw an error
# discard : eliminate a item of a set if is a member, if not do nothing

#6

A.union(B) # {19, 20, 22, 24, 25, 26, 27, 28}

#7

A.intersection(B) #{19, 20, 22, 24, 25, 26}

#8
A.issubset(B) #True A is subset of B
B.issubset(A) #False B is not a subset of A

#9

A.isdisjoint(B) #False they have items in common

#10

B.union(A)

#11

A.symmetric_difference(B)

#12

del A,B,it_companies

#13

age_set = set(age)

# print(len(age_set))
# print(len(age)) # age is bigger

#14
#Explain the difference between the following data types: string, list, tuple and set
#string = Can exist in list tuple and set, and be modified , replaced . Etc
#list = Can be modified, accept duplicates and have an order.
#tuple = Can not be modified , accept duplicates and have an order.
#set = Can be modified, dont accept duplicates  and doesnt have an order.

#15
# I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

my_sentence = 'I am a teacher and I love to inspire and teach people'

my_sentence_words = my_sentence.split()
my_sentence_set = set(my_sentence_words)

print(len(my_sentence_set)) # I have 10 unique words


















