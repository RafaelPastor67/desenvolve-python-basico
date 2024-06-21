import random
import math
n = int(input("Quantos valores? "))
soma = 0
for i in range(1, n+1):
    valor = (random.randint(0,100))
    print(f'valor {i}: {valor}')
    soma += valor
print(f'A soma dos valores é de {soma}')
print(f'A raiz quadrada é: {math.sqrt(soma)}')
    