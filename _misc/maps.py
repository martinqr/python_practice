numbers = [1,2,3,4]

numbers_v3 = list(map(lambda i: i * 2,numbers))

numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]

result = list(map(lambda x,y : x + y,numbers_1, numbers_2))

# ----------------------------------------------------------------------

items = [
    {
        'product':'camisa',
        'price': 100,
    },
    {
        'product':'pantalones',
        'price': 100
    },
    {
        'product':'pantalones 2',
        'price': 200
    }    
]

prices = list(map(lambda item: item['price'],items))


def add_taxes(item):
    new_item = item.copy() # para no modificar el dict original
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes,items))

'''
[{'product': 'camisa', 'price': 100, 'taxes': 19.0}, 
{'product': 'pantalones', 'price': 100, 'taxes': 19.0}, 
{'product': 'pantalones 2', 'price': 200, 'taxes': 38.0}]
'''
