#transformando em código o fluxograma
#Este código faz a média de 3 notas e se o resultado for maior ou igual a 60 a pessoa passou, senão se for maior ou igual a 40 é recuperação, senão reprovou
n1,n2,n3 = int(input("Digite o valor de n1: ")),int(input("Digite o valor de n2: ")),int(input("Digite o valor de n3: "))
m = (n1 + n2 + n3) /3
if m >=60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")
print("Fim")
