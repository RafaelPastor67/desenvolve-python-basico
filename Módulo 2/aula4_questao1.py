#1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.

#O terreno possui 250m2 e custa R$512,490.50

#comente na linha acima de cada instrução uma breve descrição da instrução.

#Fórmulas:
#area_m2 = comprimento * largura
#preco_total = preco_m2 * area_m2

#250m^2 = 512490.50

c = int(input("comprimento: "))
l = int(input("largura: "))
a = c*l
preço = a * 2049.962
print(f"{a}m^2, R${preço:,.2f} reais")