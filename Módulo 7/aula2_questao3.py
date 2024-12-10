frase = input("Digite uma frase: ")
frase = frase.lower()
frase = frase.replace(" ", "")
frase_invertida = ''
for i in frase[::-1]:
    frase_invertida += i
print(frase_invertida)
if frase_invertida == frase:
    print("Essa frase é um palíndromo")
else:
    print("Não é um palíndromo")