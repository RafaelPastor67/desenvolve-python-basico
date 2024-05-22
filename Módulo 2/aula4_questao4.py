valor = int(input("Digite um valor: ")) 
x = valor
nota100 = valor // 100 
valor = valor%100 
nota50 = valor//50
valor = valor%50 
nota20 = valor//20
valor = valor%20
nota10 = valor//10
valor = valor%10
nota5 = valor//5
valor = valor%5
nota2 = valor//2
valor = valor%2
nota1 =  valor//1
valor = valor%1
print(f"para o valor de R${x} Reais, serão gastos:")
print(f"{nota100} notas de 100,00")
print(f"{nota50} notas de 50,00")
print(f"{nota20} notas de 20,00")
print(f"{nota10} notas de 10,00")
print(f"{nota5} notas de 5,00")
print(f"{nota2} notas de 2,00")
print(f"{nota1} notas de 1,00")
