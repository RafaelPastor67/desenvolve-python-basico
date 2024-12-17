import os
with open ("frase.txt","r") as f:
    texto = str(f.read())
    print(texto)
    
palavras = str((texto.split()))
with open ("palavra.txt","w") as p:
        p.write(palavras)

with open ("palavra.txt","rt") as p:
    saida = p.read()
print(saida)

