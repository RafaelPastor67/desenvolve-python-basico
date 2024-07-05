lista1, lista2, lista3 = [], [], []

t1= int(input("Tamanho da lista 1: "))
for x in range(t1):
   lista1.append(int(input(f"Digite os {t1} elementos da lista 1: ")))

t2= int(input("Tamanho da lista 2: "))
for x in range(t2):
   lista2.append(int(input(f"Digite os {t2} elementos da lista 2: ")))


for i in range(max(len(lista1),len(lista2))):
   if i < len(lista1):
    lista3.append(lista1[i])
   if i < len(lista2):
    lista3.append(lista2[i])

print(lista1)
print(lista2)
print(lista3)