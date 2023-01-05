'''
1/1/23

1. Escribe una función en Python llamada ordena_palabras que tome una lista 
de palabras como argumento y devuelva la lista ordenada alfabéticamente. Por ejemplo, si la lista de entrada 
es ['gato', 'perro', 'elefante'], la función debe devolver ['elefante', 'gato', 'perro']. 

'''
def ordena_palabras (my_list):
    my_list.sort()
    print(my_list)

# ordena_palabras(['gato','perro','elefante'])

'''
2/1/23

2. Write a function called median that takes in a list of numbers and returns the median value of the list.
The median is the middle value in a sorted list of numbers, so you will need to 
first sort the list of numbers. 
If there are an even number of values in the list, return the average of the two middle values.

'''

import numpy

def median (my_list):
    my_list.sort()
    my_median = numpy.median(my_list)
    print(my_median)

# median([3,2,1,5,6,4])
# 3.5

'''
3/1/23

3. Escribe una función en Python llamada sort_words que tome una lista de palabras y 
devuelva la lista ordenada por la longitud de cada palabra. 
Si hay palabras de igual longitud, deben ordenarse alfabéticamente.

sort_words(["apple", "banana", "cherry", "date"])
# debe devolver ["date", "apple", "banana", "cherry"]

'''

def sort_words (my_list):
    my_list_sorted = sorted(my_list, key= lambda x: (len(x)))
    print(my_list_sorted)

# sort_words(["apple", "banana", "cherry", "date"])

'''
4/1/23

Crea una función sort_two_arrays(arr1, arr2) que toma dos listas ordenadas y devuelve una 
nueva lista ordenada que contiene todos los elementos de ambas listas.

'''

def sort_two_arrays(arr1,arr2):
    arr3 = arr1 + arr2
    arr3.sort()
    print(arr3)

# sort_two_arrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])


'''
5/1/23

Escribe una función en Python llamada unique_values que tenga como entrada una lista de números 
y devuelva una lista con los valores únicos de la lista de entrada. Por ejemplo:

Out put

unique_values([1, 2, 3, 3, 2, 1]) => [1, 2, 3]
unique_values([1, 2, 3]) => [1, 2, 3]

'''

def unique_values (my_list):
    my_set = set(my_list)
    new_list = list(my_set)
    print(new_list)

# unique_values([1,2,3,2,1])
