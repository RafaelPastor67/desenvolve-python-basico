idade=int(input("Qual a sua idade: "))
jogos=bool(input("Ja jogou 3 jogos?(True or False): "))
vitorias=int(input("Quantos jogos já venceu: "))
resultado = 16<= idade <=18 and jogos == True and vitorias >= 1
print(f'Apto para ingressar no clube de jogos de tabuleiro: {resultado}')