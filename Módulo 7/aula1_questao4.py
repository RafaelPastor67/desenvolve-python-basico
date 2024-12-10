numero = input("Digite um numero de celular: ")
digitos = (len(numero))

if digitos <8 or digitos >9:
    print("Número inválido")

elif digitos == 8:
    numero = "9" + numero
    digitos = len(numero)
    
if digitos == 9:
    numero = numero[:5] + "-" + numero[5:]
print("Número completo: ",numero)