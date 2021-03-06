from functools import reduce

def doble(x):
    return x+x

lista = [1, 3, -1, 15, 9]


# Map: Actuar sobre cada uno de los elementos
listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)

def esPar(x):
    return x % 2 == 0

# Filter: Filtrar los valores de "lista" que cumplan la funcion correspondiente
listaPares = filter(lambda x: x % 2 == 0, lista)
listaPares1 = filter(esPar, lista)

# Reduce:
sumatorio = reduce(lambda x, y: x + y, lista)
suma100 = reduce(lambda x, y: x + y, range(101))

# Solucionar primera posición reduce para suma
# creo copia de la lista
l = lista[:]
# añado el neutro para la suma en la posición cero
l.insert(0,0)
sumatorioDobles = reduce(lambda x, y: x + y * 2, l)


print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(sumatorioDobles)

print(suma100)