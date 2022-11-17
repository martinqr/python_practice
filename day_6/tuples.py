

# Exercises: Level 1

#1 Create an empty tuple
#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
#3 Join brothers and sisters tuples and assign it to siblings
#4 How many siblings do you have?
#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members


# Exercises: Level 2

#6 Unpack siblings and parents from family_members
#7 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
#8 Change the about food_stuff_tp tuple to a food_stuff_lt list
#9 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
#10 Slice out the first three items and the last three items from food_staff_lt list
#11 Delete the food_staff_tp tuple completely

# ////////////////////////////////////////////////////////////////////// #

# Check if an item exists in tuple:

#12 Check if 'Estonia' is a nordic country
#13 Check if 'Iceland' is a nordic country

# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

#1

my_tuple = ()

#2

my_sisters = ('Micaela','Noelia')
my_brothers = ('Nicolas','Joaquin')

#3

my_siblings = my_sisters + my_brothers

#4

len(my_siblings)

#5

family_members = my_siblings + ('Stella','Matias')

#6

siblings = family_members[0:4]
parents = family_members[4::]

#7

fruits = ('Orange','Banana','Strawberry','Apple')
vegetables = ('Potato','Onion','Carrot','Corn')
animal_products = ('Egg','Milk','Cheese','Yogurt')

food_stuff_tp = fruits + vegetables + animal_products

#8

food_stuff_tp = list(food_stuff_tp)
food_stuff_lt = food_stuff_tp

#9

middle_item = food_stuff_lt[(int(len(food_stuff_lt) / 2))]

#10

first_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[9:]

#11

del food_stuff_tp

#12 y 13

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# find_1 = nordic_countries.index('Estonia')
find_2 = nordic_countries.index('Iceland')


















