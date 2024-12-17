import os

with open("estomago.txt", "r", encoding="latin-1") as arquivo:
    linhas = arquivo.readlines()


print("As primeiras 25 linhas do arquivo:")
for i in range(min(25, len(linhas))):
    print(linhas[i].strip()) 

print("\n" + "-" * 50 + "\n")


num_linhas = len(linhas)
print(f"O número total de linhas no arquivo é: {num_linhas}")


linha_mais_longa = max(linhas, key=len)
print("\nA linha com maior número de caracteres é:")
print(linha_mais_longa.strip())
print(f"Número de caracteres: {len(linha_mais_longa)}")


texto_completo = " ".join(linhas).lower() 


palavras = texto_completo.split()
menções_nonato = sum(1 for palavra in palavras if palavra == "nonato")


menções_iria = sum(1 for palavra in palavras if palavra == "íria")

print("\nNúmero de menções aos personagens:")
print(f"Nonato: {menções_nonato}")
print(f"Íria: {menções_iria}")
