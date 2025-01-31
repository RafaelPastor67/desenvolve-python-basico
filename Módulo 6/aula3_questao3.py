import random

lista = [-1, -2, -3, 5, -4, -5, -6, -7, 2, -8, -9]
print(lista)
contador = []
sequencia_max = []
for indice, i in enumerate(lista):
    if i<0:
        contador.append(indice)
        if len(contador) > len(sequencia_max):
            sequencia_max = contador
    else:
        contador = []
print(lista.index(sequencia_max))
print(lista.index(contador))
print(lista)

#random.randint(-10, 10) for i in range(20)