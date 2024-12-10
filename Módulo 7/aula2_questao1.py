meses = [
    "Janeiro", 
    "Fevereiro", 
    "Março", 
    "Abril", 
    "Maio", 
    "Junho", 
    "Julho", 
    "Agosto", 
    "Setembro", 
    "Outubro", 
    "Novembro", 
    "Dezembro"
]

data = input("Digite uma data de nascimento no formato dd/mm/aaaa: ")
dia,ano = data[0:2],data[6:10]
mes_extenso = int(data[3:5]) - 1

print(f"Você nasceu em  {dia} de {meses[mes_extenso]} de {ano}")
