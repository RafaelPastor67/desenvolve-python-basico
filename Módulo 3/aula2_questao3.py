idade=int(input("Qual a sua idade: "))
jogos=bool(input("Ja jogou 3 jogos?: "))
vitorias=int(input("Quantos jogos já venceu: "))
if idade >= 16 and idade <= 18:
    if jogos == True:
        if vitorias > 0:
            print("True")
        else:
            print("false")  
    else:
        print("false")
else:
    print("false")
    