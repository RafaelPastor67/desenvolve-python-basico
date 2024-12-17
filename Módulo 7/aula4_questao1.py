import os
frase = input("Digite uma frase: ")
with open("frase.txt","w",encoding="UTF-8") as f:
    f.write(frase)
print(f"Caminho salvo em {os.path.abspath("frase.txt")}")