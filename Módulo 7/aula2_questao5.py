import random


def embaralhar_palavras(frase):
    palavras = []
    palavra_string = ""

    for caractere in frase:
        if caractere == " ":
            if palavra_string:
                palavras.append(palavra_string)
                palavra_string = ""
        else:
            palavra_string += caractere
    if palavra_string:
        palavras.append(palavra_string)

    resultado=[]
    for palavra in palavras:
        if len(palavra) > 3:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            nova_palavra = palavra[0] + ''.join(meio) + palavra[-1]
        else:
            nova_palavra = palavra
        resultado.append(nova_palavra)

    return' '.join(resultado)

frase = input("Escreva uma frase para embaralhar: ")
resultado = embaralhar_palavras(frase)
print(resultado)

