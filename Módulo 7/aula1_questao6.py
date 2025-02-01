frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra-objetivo: ")
anagramas = []
palavra_ordenada = sorted(palavra.lower())
for i in frase.split():
    sorted_i = sorted(i.lower())
    if sorted_i == palavra_ordenada:
        anagramas.append(i)
print(anagramas)