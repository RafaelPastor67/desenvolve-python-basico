# Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if ((n1+n2) % 2) != 0: #soma os numeros e se o resto da divisão não for zero significa que o número é impar 
    p = "Ímpar"
else: #senão é par
    p= "Par"
print(f"O número digitado é {p}")
