'''
Importing a Module
To import the file we use the import keyword and the name of the file only.
'''
from random import random, randint
import random,string


# print(mymodule.generate_full_name('martin','zalazar'))
# print(mymodule.sum_two_nums(2,3))

'''
Exercises: Level 1
Writ a function which generates a six digit/character random_user_id
'''

user_id = []

def random_user_id():
    while len(user_id) < 6:
        for i in random.choice(string.digits):
            user_id.append(i)
        for i in random.choice(string.ascii_lowercase):
            user_id.append(i)
    user_id_str = ''
    for i in user_id:
        user_id_str += i
    return user_id_str

# print(random_user_id())

'''
Modify the previous task. Declare a function named user_id_gen_by_user. It doesnt take any parameters but it takes two inputs using input(). 
One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
'''

def user_id_gen_by_user():
  num_chars = int(input("Enter the number of characters for the ID: "))

  num_ids = int(input("Enter the number of IDs to generate: "))

  for i in range(num_ids):
    id = ""
    for j in range(num_chars):
      id += random.choice(string.ascii_letters + string.digits)
    return

# print(user_id_gen_by_user())


'''
Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
'''

def rgb_color_gen():
    return 'rgb'+ '(' + str(randint(0, 255))+','+ str(randint(0, 255))+','+ str(randint(0, 255)) + ')'


# print(rgb_color_gen())

'''
Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
Write a function generate_colors which can generate any number of hexa or rgb colors.
generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
'''

# Hexa colors

def list_of_hexa_colors():
    hexa = "#"
    for j in range(3):
        hexa += random.choice(string.ascii_letters[:6]) + random.choice(string.digits[:9] )
    return hexa

print(list_of_hexa_colors())