import random
lista1, lista2, inters=[], [], []

for i in range(20):
    lista1.insert(i,random.randint(0,50))
    lista2.insert(i,random.randint(0,50))

for elemento in lista1:
    if elemento in lista2 and elemento not in inters:
        inters.append(elemento)
    
inters.sort()

print(sorted(lista1))
print(sorted(lista2))
print(inters)
for i in inters:
    print(f"{i}: ({lista1.count(i)}),({lista2.count(i)})")
