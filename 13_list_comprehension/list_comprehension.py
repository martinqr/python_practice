'''
Exercises
'''
# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

my_numbers = [i for i in numbers if i <= 0]

#################################################################

# 2. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

'''
output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

my_new_list = [number for row in list_of_lists for number in row] # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_final_list = [number for row in my_new_list for number in row] # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#################################################################

# 3. Using list comprehension create the following list of tuples:

tuples = [(n, 1, n**2, n**3, n**4, n**5, n**6) for n in range(11)]

print(tuples)



# 5. Change the following list to a list of dictionaries

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

'''
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
'''

my_dict = [{'countries': i[0][0] , 'city': i[0][1]} for i in countries]

#################################################################

# 6. Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

'''
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
'''

my_first_name = [name[0] + ' ' + name[1] for row in names for name in row] # ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

#################################################################

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.

calculate_slope = lambda x1,y1,x2,y2: int((y2 - y1) / (x2 -x1))





