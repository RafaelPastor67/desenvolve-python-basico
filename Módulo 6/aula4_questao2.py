entrada = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
lista_vogais=sorted([x for x in entrada if x in vogais])
lista_consoante=[x for x in entrada if x.isalpha() and x not in vogais]
print(lista_vogais)
print(lista_consoante)