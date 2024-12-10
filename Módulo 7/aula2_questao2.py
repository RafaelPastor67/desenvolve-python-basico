frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
frase_modificada = ''

for i in frase:
    if i in vogais:
        frase_modificada += '*'
    else:
        frase_modificada+=i
        

print(frase_modificada)