#Entrada
d = int(input("Distancia em Km: "))
peso = int(input("Peso do pacote em Kg: "))

if d > 300:
    valor = 2 * peso
elif 300 >= d > 100:
    valor = float(1.5 * peso)
else:
    valor = 1 * peso
if peso >= 10:
    valor += 10
print(f"O valor do frete é de R${valor:,.2f} Reais")