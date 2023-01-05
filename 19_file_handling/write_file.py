def write_file (my_list):
    with open('PATH DE TU ARCHIVO', 'w') as txt_file_2:
        for i in my_list:
            txt_file_2.write(f'{i}\n')


write_file(['jose','luis','jorge'])

'''
#out put

jose
luis
jorge

'''