frase = input("Digite uma frase: ")

indices = []
vogais = "aeiouAEIOU"

for i, letra in enumerate(frase):
    if letra in vogais:
        indices.append(i)
        
print(f"{len(indices)} Vogais")
print(f"Indices: {indices}")