# funcion para incrementar por 1 el valor ingresado
def increment (x):
    return x + 1

# high order function , que toma como parametro una funcion
def high_ord_func (x,func):
    return func(x)

# ingreso como primer parametro el 2 que seria x y como segundo parametro la funcion increment.
print(high_ord_func(2,increment))
# 3