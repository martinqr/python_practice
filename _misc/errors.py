#print(0/0)
#print(result)
# print('hola')

# suma = lambda x,y: x + y

# #if condition returns True, then nothing happens:
# # assert suma(2,2) == 4

# # #if condition returns False, AssertionError is raised:
# # assert suma(2,2) == 5


# # Realizar una exception si la condicion se cumple y cortar la ejecucion.
# age = 10

# if age < 18:
#     raise Exception('No se permiten menores de edad')


'''
____________________________________________________________________________
____________________________________________________________________________

'''

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
    print(error)

