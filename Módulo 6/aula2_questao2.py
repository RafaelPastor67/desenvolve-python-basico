import random

num_elementos = random.randint(5, 20)
elementos = []
for i in range(num_elementos):
    elementos.insert(i,random.randint(1,10))
soma_lista = sum(elementos)
media_lista = soma_lista / len(elementos)
print(f'A lista tem {num_elementos} valores')
print(elementos)
print(f'A soma de todos os valores é: {soma_lista}')
print(f'A média dos valores: {media_lista}')
