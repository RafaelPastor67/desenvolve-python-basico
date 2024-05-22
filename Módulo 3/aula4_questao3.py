#verificar se o ano é bissexto

#Entrada de dados
n=int(input("Digite um ano: "))

if (n % 4) == 0 and (n % 100) != 0 or (n % 400) == 0: #se o ano for divisível por 4 e não for divisível por 100, ou se for divisível por 400 vai ser bissexto
    n= "Bissexto"
else:
    n = "Não bissexto"
print(n)