lista=[]
for _ in range(5):
    lista.append(int(input("Entre com valores: ")))

print(f"Lista: {lista}")
print(f"Os 3 primeiros valores: {lista[:3]}")
print(f"Os 2 últimos valores: {lista[-2:]}")
print(f"A lista invertida: {lista[::-1]}")
print(f"Elementos de índice par: {lista[::2]}")
print(f"Elementos de índice ímpar: {lista[1::2]}")


