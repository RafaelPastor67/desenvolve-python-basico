# calcular a média de idade dos respondentes. Escreva um programa que leia um inteiro N com a quantidade de respondentes
#  e em seguida leia as N idades de cada respondente. Ao final, imprima a média das idades
n = int(input("Quantos respondentes: "))
b = n
soma = 0
while n>0:
    x=int(input('Idade do respondente: '))
    soma += x
    n=n-1
print(soma/b)
