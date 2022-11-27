import math

#1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers (number_one,number_two):
    return number_one + number_two


#2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle (radius):
    return 3,14 * radius + radius

#3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums (*numbers):
        total = 0
        for num in numbers:
            total += num
        return total

# print(add_all_nums(2,2,2))

#4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

# def convert_celsius_to_fahrenheit (c):
#     result = f = (c * 9/5) + 32
#     return result


# print(convert_celsius_to_fahrenheit(26))

#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# The seasons are defined as spring (March, April, May), summer (June, July, August), 
# autumn (September, October, November) and winter (December, January, February).

def check_season(month):
    month_lower = month.lower()
    if month_lower == 'march' or month_lower == 'april' or month_lower == 'may':
        return 'Spring'
    elif month_lower == 'june' or month_lower == 'july' or month_lower == 'august':
        return 'Summer'
    elif month_lower == 'september' or month_lower == 'october' or month_lower == 'november':
        return 'autumn'
    elif month_lower == 'december' or month_lower == 'january' or month_lower == 'february':
        return 'winter'
    else:
        return 'Not a valid month'

# print(check_season('March'))

#6 Write a function called calculate_slope which return the slope of a linear equation

# (x₁, y₁) = (-1, 5)
# (x₂, y₂) = (1, 1)
# Slope, m = (y₂ - y₁) / (x₂ - x₁)
# = (1 - 5) / (1 - (-1))
# = -4/2
# = -2

# def calculate_slope (x1,y1,x2,y2):
#     result = (y2 - y1) / (x2 -x1)
#     return result

# print(calculate_slope(-1,5,1,1))

#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

# def solve_quadratic_eqn(a,b,c):
#     x1 = (b * -1 + (math.sqrt((b**2) - (4 * a * c)))) / 2 * a
#     x2 = (b * -1 - (math.sqrt((b**2) - (4 * a * c)))) / 2 * a
#     result = f'x1: {x1} and x2: {x2}'
#     return  result

# print(solve_quadratic_eqn(1,6,9))

#8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

# def my_list (*list):
#     return [list]

# print(my_list('hola','adios'))

#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

# def reverse_list (*list):
#     my_reverse = []
#     for i in list:
#         my_reverse.append(i)
#     my_reverse.reverse()
#     return my_reverse

# print(reverse_list('hola','adios'))

#10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

# def capitalize_list_items(*list):
#     my_capital = []
#     for i in list:
#         my_capital.append(i.capitalize())
#     return my_capital 

# print(capitalize_list_items('hola','adios'))


#11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']

# def add_item (my_list,my_item):
#     my_new_list = my_list
#     my_list.append(my_item)
#     return my_new_list

# print(add_item(food_staff,'Apple'))

#12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

# def remove_item (my_list,del_item):
#     my_new_list = my_list
#     my_list.remove(del_item)
#     return my_new_list

# print(remove_item(food_staff,'Potato'))

#13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

# def sum_of_numbers(num):
#    my_sum = sum(range(num + 1))
#    return my_sum

# print(sum_of_numbers(100))

#14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

# def sum_of_odds (num):
#     x = range(num + 1)
#     my_list_range = []
#     my_sum_odds = []
#     for i in x:
#         my_list_range.append(i)
#     for i in my_list_range:
#         if i % 2 == 0:
#             continue
#         elif i % 2 != 0:
#             my_sum_odds.append(i)

#     return sum(my_sum_odds)

# print(sum_of_odds(10))

#15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

# def sum_of_even (num):
#     x = range(num + 1)
#     my_list_range = []
#     my_sum_even = []
#     for i in x:
#         my_list_range.append(i)
#     for i in my_list_range:
#         if i % 2 != 0:
#             continue
#         elif i % 2 == 0:
#             my_sum_even.append(i)

#     return sum(my_sum_even)

# print(sum_of_even(10))

# Exercises Level 2

#1 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

# def evens_and_odds (num):
#     x = range(num + 1)
#     my_all_numbers = []
#     my_even_numbers = []
#     my_odd_numbers = []
#     for i in x:
#         my_all_numbers.append(i)
#     for i in my_all_numbers:
#         if i % 2 != 0:
#             my_odd_numbers.append(i)
#         elif i % 2 == 0:
#             my_even_numbers.append(i)
#     len_even_numbers = len(my_even_numbers)
#     len_odd_numbers = len(my_odd_numbers)
#     return f'The number of odds are: {len_odd_numbers} , The number of evens are: {len_even_numbers}'

# print(evens_and_odds(100))

#1 Call your function factorial, it takes a whole number as a 
# parameter and it return a factorial of the number
#The factorial of a whole number is the function that multiplies the number by every natural number below it

# def fact_of_number(num):
#     x = range(1,num + 1)
#     my_number_range = []
#     for i in x:
#         my_number_range.append(i)

#     return math.prod(my_number_range)


# print(fact_of_number(4))

#2 Call your function is_empty, it takes a parameter and it checks if it is empty or not

# food_truck = []

# def is_empty(my_input):
#     if len(my_input) == 0:
#         return 'Is Empty'
#     else:
#         return 'Is something'

# print(is_empty(food_truck))


#3 Write different functions which take lists. They should calculate_mean, 
# calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

# The mean x̄ of a data set is the sum of all the data divided by the count n.
# The median x˜ is the data value separating the upper half of a data set from the lower half.
# the mode is the value or values in the data set that occur most frequently.
# the range


data_set = [9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]

def calculate_mean (my_data):
    my_mean = sum(my_data) / len(my_data)
    return my_mean

# print(calculate_mean(data_set))

def calculate_median (my_data):
    my_first_median = my_data[int((len(my_data) / 2) - 1)]
    my_second_median = my_data[int(len(my_data) / 2)]
    my_diference_value = my_first_median - my_second_median
    my_median = (my_diference_value / 2) + my_second_median

    return my_median

# print(calculate_median(data_set))

# SOLO SIRVE PARA EL 1ER VALOR QUE SE REPITA MAS VECES EN UNA LISTA, SI HAY MAS DE UNO TOMA EL PRIMERO.
# EJEMPLO : data_set = [9, 10, 12,12,12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25] 
# TANTO EL 12 COMO EL 13 SON LO QUE MAS SE REPITEN, CADA UNO 3 VECES PERO LA FUNCION SOLO VA A TOMAR COMO 12 COMO EL UNICO VALOR QUE MAS SE REPITE.
# UTILIZAR UNA LIBRERIA PARA TENER MAS UN VALOR QUE SE REPITA.

def calculate_mode (my_data):
    my_values = []
    my_occurs = []
    # CARGO LOS VALOR DEL PARAMETRO EN UNA LISTA NUEVA
    for i in my_data:
        my_values.append(i)
    # CARGO LAS VECES QUE SE REPITE CADA VALOR EN MY_OCCURS
    for i in my_values:
        my_occurs.append(my_values.count(i))
    # PASO TODOS LOS NUMEROS EN MY_OCCURS A STRING
    my_occurs_string = map(str,my_occurs)
    my_occurs_string = list(my_occurs_string)
    # BUSCO EL INDICE DEL VALOR MAS GRANDE EN MY_OCCURS_STRING.
    for i in my_occurs_string:
       my_occurs_max_index = my_occurs_string.index(str(max(my_occurs)))
    # RETORNO EL VALOR DEL NUMERO QUE MAS SE REPITE
    return my_values[my_occurs_max_index]

# print(calculate_mode(data_set))


def calculate_range(my_data):
   my_min = min(my_data)
   my_max = max(my_data)

   return my_max - my_min

# print(calculate_range(data_set))


# Exercises : Level 3

#1 Write a function called is_prime, which checks if a number is prime.

# def is_prime (num):
#     for i in range(2, int(num/2)+1):
#         if (num % i) == 0:
#             return "Is not a prime number"
#     else:
#         return "Is a prime number"

# print(is_prime(5))

#2 Write a functions which checks if all items are unique in the list.

data_set = [9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]

data_1 = [1,2,3,4,5,6,1,2,3,4,5,6]
data_2 = [1,2,3,4,5,6]
data_3 = ['hola','adios','hola']
data_4 = ['hola','adios','chau']
 
 
def check_unique (my_data):
    my_new_data = []
    for i in my_data:
        if i in my_new_data:
            return 'Not unique'
            break
        if i not in my_new_data:
            my_new_data.append(i)
    else:
        return 'Unique'
 
# print(check_unique(data_2))