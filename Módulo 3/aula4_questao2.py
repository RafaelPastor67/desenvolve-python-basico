#2) Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários.
# Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve imprimir uma mensagem correspondente à classificação do filme:

n=int(input("Digite uma nota de 1 a 5 para o filme: "))

if n == 1:
    print("O filme é Ruim")
elif n==2:
    print("O filme é Regular")
elif n==3:
    print("O filme é Bom!")
elif n==4:
    print("O filme é Muito bom!")
elif n==5:
    print("O filme é Excelente!")
else:
    print("Nota inválida")

