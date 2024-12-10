import random

def encrypt(lista, encode):
    lista_crip = []  
    for i in lista:
        letras_crip = []
        for j in i:
            x = ord(j) + encode  
           
            x = 33 + (x - 33) % 94
            letras_crip.append(chr(x))  
        lista_crip.append(''.join(letras_crip))  
    return lista_crip


nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
encode = random.randint(1, 10) 


nomes_criptografados = encrypt(nomes, encode)


print(f"Chave de criptografia: {encode}")
print(f"Nomes criptografados: {nomes_criptografados}")