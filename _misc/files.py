with open('./text.txt' , 'r+') as file:
    for line in file:
        print(line)
    file.write('nueva linea \n')

# 'r+ permite tanto leer como escribir
# 'w+' reescribe el archivo por las lineas nuevas



# file.close() # cierra el archivo

# print(file.read())
# print(file.readline()) # lee por linea