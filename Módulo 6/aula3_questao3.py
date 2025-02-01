import random

lista = [random.randint(-10, 10) for i in range(20)]
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
print(sequencia_max)
del(lista[sequencia_max[0]:sequencia_max[-1]+1])
print(lista)
