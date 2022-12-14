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

4. Crea una función sort_two_arrays(arr1, arr2) que toma dos listas ordenadas y devuelve una 
nueva lista ordenada que contiene todos los elementos de ambas listas.

'''

def sort_two_arrays(arr1,arr2):
    arr3 = arr1 + arr2
    arr3.sort()
    print(arr3)

# sort_two_arrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])


'''
5/1/23

5. Escribe una función en Python llamada unique_values que tenga como entrada una lista de números 
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

'''
6/1/23

6. Implementa una función contar_vocales(texto) que tome una cadena de texto y 
devuelva un diccionario con las vocales como claves y el número de veces que aparecen 
en el texto como valores. La función debe ignorar mayúsculas y minúsculas.

'''

texto = "Hola, mundo"

vocals = {'a':0,
        'e':0,
        'i':0,
        'o':0,
        'u':0}


def contar_vocales(my_str):
    my_str_low = my_str.lower()
    for letter in my_str_low:
        if letter in vocals:
            vocals[letter] += 1
    new_vocals= {x:y for x,y in vocals.items() if y!=0}
    print(new_vocals)

# contar_vocales(texto)

''''
7/1/23

7. Escribe una función top_words(text: str, k: int) -> List[str] que devuelva una lista con las k 
palabras más comunes en text.

top_words(text, 2)

out put 

['ejemplo', 'de']

'''

from collections import Counter

text = "Este es un ejemplo de texto de ejemplo."

def top_words (text: str,k:int):
    to_lower = text.lower()
    my_list = sorted(to_lower.split())
    my_counter = Counter(my_list).most_common(k)
    print(my_counter)

# top_words(text,2)
# [('de', 2), ('ejemplo', 1)]

'''
8/1/23

8. Escribe una función llamada "invertir_diccionario" que tome un diccionario como argumento y devuelva un nuevo diccionario 
donde las claves y valores han sido intercambiados. Por ejemplo:

>>> invertir_diccionario({'a': 1, 'b': 2, 'c': 3})
{1: 'a', 2: 'b', 3: 'c'}
>>> invertir_diccionario({'foo': 'bar', 'hello': 'world'})
{'bar': 'foo', 'world': 'hello'}
'''

def invertir_diccionario (dct):
    new_dct = {x:y for y,x in dct.items()}
    print(new_dct)

#invertir_diccionario({'a': 1, 'b': 2, 'c': 3})


'''
9/1/23

9. Write a program which will find all such numbers which are divisible by 7 but 
are not a multiple of 5, between 2000 and 3200 (both included). 
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
lst = []
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0 :
        lst.append(str(i))
    else:
        continue
#print(lst)

'''
10/1/23

10. Se tienen los resultados de una encuesta de satisfacción en una empresa en forma de un diccionario,
# donde cada clave es el nombre del empleado y el valor es una lista con sus respuestas a una escala de 1 a 5.

resultados = {
    "Juan": [4, 3, 5, 4, 4],
    "Maria": [5, 5, 4, 3, 5],
    "Pedro": [5, 4, 4, 3, 5],
    "Ana": [4, 4, 4, 5, 5],
    "Lucia": [5, 5, 4, 5, 3]
}

# Se desea calcular el promedio de la encuesta para cada empleado y almacenarlo en un nuevo diccionario,
# donde cada clave es el nombre del empleado y el valor es el promedio de sus respuestas.
# Crear una funcion para calcular el promedio y otra para mostrar los promedios

'''

import numpy

resultados = {
    "Juan": [4, 3, 5, 4, 4],
    "Maria": [5, 5, 4, 3, 5],
    "Pedro": [5, 4, 4, 3, 5],
    "Ana": [4, 4, 4, 5, 5],
    "Lucia": [5, 5, 4, 5, 3]
}

def calcular_promedio (lst):
    dct = {}
    for i in lst:
        dct[i] = numpy.average(lst[i])
    print(dct)

# calcular_promedio(resultados)
# {'Juan': 4.0, 'Maria': 4.4, 'Pedro': 4.2, 'Ana': 4.4, 'Lucia': 4.4}

'''
11/1/23

11. Dado un diccionario que contiene como claves los nombres de productos y como valores una tupla 
con su precio y su stock, crear una función que calcule el valor total en inventario de todos los productos.

'''

inventario = {"producto1": (10, 5), "producto2": (15, 3), "producto3": (20, 2)}

def calcular_valor_total (products):
    total = 0
    for i in products:
        total += products[i][0] * products[i][1]
    print(total)

#calcular_valor_total(inventario)

'''
12/1/23

12. Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
Suppose the following input is supplied to the program: 8 Then, 
the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''
def product_of (integral):
    dct = {}
    for i in range(1,integral + 1):
        dct[i]= i*i
    print(dct)

#product_of(8)