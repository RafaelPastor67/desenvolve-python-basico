import csv 

#importa os csv's para nosso script
usuarios_csv = r'./Trabalho-Prático/user.csv'
produtos_csv = r'./Trabalho-Prático/product.csv'

# Função para adicionar um usuário

def adicionar_dados_csv(arquivo, dados):
   
    with open(arquivo, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)    
        writer.writerow(dados)

def criarconta():
    novo_usuario = input("Nome de Usuário: ")
    nova_senha = input('Senha: ')
    novo_nome = input("Nome: ")
    dados_novo_usuario=[novo_usuario,novo_nome,nova_senha,'cliente']
    adicionar_dados_csv(usuarios_csv,dados_novo_usuario)
    print("\nConta criada com sucesso!")

dados_dict = {}

with open(usuarios_csv, mode='r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)  # Lê o CSV como um dicionário
    for coluna in leitor:
        usuario = coluna.pop("user")
        dados_dict[usuario] = coluna

barrinhas = "---------------------------"

print("1. Entrar \n2. Criar conta \n3. Sair \n",barrinhas)
d1=input("Escolha uma opção: ")
print('')
if d1 == '1':

    usuario_digitado = input("Usuario: ")
    if usuario_digitado in dados_dict:
        senha_digitada = input('Senha: ') 
        if senha_digitada in {dados_dict[usuario_digitado]['Password']}:
            print(f'\nBem Vindo, {dados_dict[usuario_digitado]["Nome"]}!')
            print('')
            d2=input()


        else:
            print("Senha Incorreta!")
    else:
        print("Esse usúario não existe!")
elif d1=='2':
    criarconta()
elif d1 == '3':
    print("Programa Encerrado!")
    
else:
    print("Opção inválida")


