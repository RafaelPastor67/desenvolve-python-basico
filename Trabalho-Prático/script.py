import csv 

#importa os csv's para nosso script
usuarios_csv = r'./Trabalho-Prático/user.csv'
produtos_csv = r'./Trabalho-Prático/product.csv'

#Dicionario onde vai ser armazenado os dados dos csv's
dados_dict = {}
produtos_dict = {}

with open(usuarios_csv, mode='r', encoding='utf-8') as arquivo: #Transforma o csv USER em dicionario
    leitor = csv.DictReader(arquivo)  # Lê o CSV como um dicionário
    for coluna in leitor:
        usuario = coluna.pop("user")
        dados_dict[usuario] = coluna

with open(produtos_csv, mode='r', encoding='utf-8') as arquivo: #Transforma o csv PRODUCT em dicionario
    leitor = csv.DictReader(arquivo)  # Lê o CSV como um dicionário
    for coluna in leitor:
        codigo = coluna.pop("codigo")
        produtos_dict[codigo] = coluna

#Função que encerra o programa
def programa_encerrado():
    print("Programa Encerrado!")

#Lê o CSV e preenche com os dados
def adicionar_dados_csv(arquivo, dados):
   
    with open(arquivo, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)    
        writer.writerow(dados)

#Cria um novo usuário e adiciona ao CSV por meio da função adicionar_dados_csv acima
def criar_novo_usuario(role):        
    novo_usuario = input("Nome de Usuário: ")
    nova_senha = input('Senha: ')
    novo_nome = input("Nome: ")
    dados_novo_usuario=[novo_usuario,novo_nome,nova_senha,role]
    adicionar_dados_csv(usuarios_csv,dados_novo_usuario)
    print("\nConta criada com sucesso!")

#Igual a função acima, porém para produtos, ela é diferente pois o id é gerado automaticamente
def adicionar_produto():
    # Obter o maior ID atual no arquivo CSV
    maior_id = 0
    with open(produtos_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for linha in reader:
            try:
                maior_id = max(maior_id, int(linha['codigo']))
            except ValueError:
                continue

    # Criar o novo produto com ID único
    novo_produto = input("Nome do Produto: ")
    novo_preco = input("Preço: ")
    id_unico = maior_id + 1
    dados_novo_produto = [id_unico, novo_produto, novo_preco]

    # Adicionar ao CSV
    adicionar_dados_csv(produtos_csv, dados_novo_produto)
    print(f"\nProduto adicionado com sucesso! ID: {id_unico}")

def mostrarestoque():#Transforma o csv produducts em dicionario
    with open(produtos_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        print("\n### Lista de Produtos ###")
        for linha in leitor:
            print(f"Código: {linha['codigo']} | {linha['produto']} | Preço: R${linha["preço"]}")
            produtos_dict = linha
        return(produtos_dict)

def mostrarusuario():#imprime o dicionario de usuarios formatado para facil leitura
    print("\n### Lista de Usuários ###\n")
    for user,dados in dados_dict.items():
        nome = dados.get("Nome")
        senha = dados.get("Password")
        role = dados.get("Role")
        print(f"{user} | Nome: {nome} | Senha: {senha} | Cargo: {role}")

def excluirproduto():
    codigo = input("Digite o código do produto que deseja excluir: ")
    linhas_atualizadas = []
    produto_encontrado = False

    with open(produtos_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        campos = leitor.fieldnames
        for linha in leitor:
            if linha['codigo'] != codigo:
                linhas_atualizadas.append(linha)
            else:
                produto_encontrado = True

    if produto_encontrado:
        with open(produtos_csv, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(linhas_atualizadas)
        print(f"Produto com código {codigo} removido com sucesso!")
    else:
        print("Produto não encontrado!")

def excluirusuario():
    usuario = input("Digite o nome de usuario que deseja excluir: ")
    linhas_atualizadas = []
    usuario_encontrado = False

    with open(usuarios_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        campos = leitor.fieldnames
        for linha in leitor:
            if linha['user'] != usuario:
                linhas_atualizadas.append(linha)
            else:
                usuario_encontrado = True

    if usuario_encontrado:
        with open(usuarios_csv, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(linhas_atualizadas)
        print(f"Usuario {usuario} removido com sucesso!")
    else:
        print("Usuário não encontrado!")        

def editar_produto():
    codigo = input("Digite o código do produto que deseja editar: ")
    linhas_atualizadas = []
    produto_encontrado = False

    with open(produtos_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        campos = leitor.fieldnames
        for linha in leitor:
            if linha['codigo'] == codigo:
                produto_encontrado = True
                print(f"Produto encontrado: {linha['produto']} - Preço: R${linha['preço']}")
                novo_nome = input("Digite o novo nome do produto (deixe vazio para manter o atual): ") or linha['produto']
                novo_preco = input("Digite o novo preço do produto (deixe vazio para manter o atual): ") or linha['preço']
                linha['produto'] = novo_nome
                linha['preço'] = novo_preco
                print("Produto atualizado com sucesso!")
            linhas_atualizadas.append(linha)

    if produto_encontrado:
        with open(produtos_csv, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(linhas_atualizadas)
    else:
        print("Produto não encontrado!")

def editar_usuario():
    user = input("Digite o usuario que deseja editar: ")
    linhas_atualizadas = []
    user_encontrado = False

    with open(usuarios_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        campos = leitor.fieldnames
        for linha in leitor:
            if linha['user'] == user:
                user_encontrado = True
                print(f"Usuario encontrado: {linha['user']} -Senha: {linha['Password']} - Nome: {linha['Nome']} - Role: {linha['Role']}")
                novo_usuario = input("Digite o novo nome de usuário (deixe vazio para manter o atual): ") or linha['user']
                novo_nome = input("Digite o Nome completo (deixe vazio para manter o atual): ") or linha['Nome']
                nova_Senha = input("Digite a nova senha (deixe vazio para manter o atual): ") or linha['Password']
                novo_cargo = input("Digite o novo cargo (Admin,Employer,cliente) (deixe vazio para manter o atual): ") or linha['Role']
                linha['user'] = novo_usuario
                linha['Nome'] = novo_nome
                linha['Password'] = nova_Senha
                linha['Role'] = novo_cargo
                print("usuário atualizado com sucesso!")
            linhas_atualizadas.append(linha)

    if user_encontrado:
        with open(usuarios_csv, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(linhas_atualizadas)
    else:
        print("Usuario não encontrado!")

def menuadmin(escolha):

    if escolha == "1":
        escolha2 = input("1. Ver estoque\n2. Ver Usuários\nEscolha uma opção: ")
        if escolha2 == '1':
            mostrarestoque()
        if escolha2 == '2':
             mostrarusuario()

    elif escolha == '2':
        escolha2 = input("1. Adicionar Produto\n2. Remover Produto\n3. Editar Produto\nEscolha uma opção: ")
        if escolha2 == '1':
            adicionar_produto()
        elif escolha2 == '2':
            excluirproduto()
        elif escolha2 == '3':
            editar_produto()

    elif escolha == '3':
        escolha2 = input("1. Criar Usuário\n2. Remover Usuário\n3. Editar Usuário\nEscolha uma opção: ")
        if escolha2 == '1':
            role = input("Qual o cargo do novo usuário?(Admin,Employer,cliente): ")
            criar_novo_usuario(role)
        elif escolha2 == '2':
            excluirusuario()
        elif escolha2 == '3':
            editar_usuario()

    elif escolha == '4':
        programa_encerrado()

def menuemployer(escolha):
    if escolha == "1":
        mostrarestoque()
    elif escolha == '2':
        escolha2 = input("1. Adicionar Produto\n2. Remover Produto\n3. Editar Produto\nEscolha uma opção: ")
        if escolha2 == '1':
            adicionar_produto()
        elif escolha2 == '2':
            excluirproduto()
        elif escolha2 == '3':
            editar_produto()
    
def menucliente():
    print("Você só tem permissão para ver o catálogo")
    mostrarestoque()

barrinhas = "---------------------------"
#############################################################################################################################################################################
print("1. Entrar \n2. Criar conta \n3. Sair \n",barrinhas)
d1=input("Escolha uma opção: ")
print('')
            
if d1 == '1': #Se o usuario escolher a opção 1, vai pedir o nome de usuario, se exister no user.csv vai pedir a senha e comparar se é a correta então o codigo vai prosseguir

    usuario_digitado = input("Usuario: ")
    if usuario_digitado in dados_dict:
        senha_digitada = input('Senha: ') 

        if senha_digitada in {dados_dict[usuario_digitado]['Password']}:
            print(f'\nBem Vindo, {dados_dict[usuario_digitado]["Nome"]}!')
            print(f'Você é {dados_dict[usuario_digitado]["Role"]}\n')

            if dados_dict[usuario_digitado]["Role"] == 'Admin':
                print("O que você deseja?\n\n1. Ver estoque/lista de usúarios\n2. Adicionar/Remover/Editar Estoque\n3. Criar/Remover/Editar usuários\n4. Sair\n",barrinhas)
                escolha= input("Escolha uma opção: ")
                menuadmin(escolha)

            elif dados_dict[usuario_digitado]["Role"] == 'Employer':
                print("O que você deseja?\n1. Ver estoque\n2. Adicionar/Remover/Editar Estoque\n3. Sair\n",barrinhas)
                escolha= input("Escolha uma opção: ")
                menuemployer(escolha)

                escolha= input("Escolha uma opção: ")
            elif dados_dict[usuario_digitado]["Role"] == 'cliente':
                menucliente()

        else:
            print("Senha Incorreta!")
    else:
        print("Esse usúario não existe!")
        
elif d1=='2': #Se o usuario escolher a opção2, vai criar um novo usuário, com a role (Cliente) e adicionar todos os dados no csv user.csv
    role = 'cliente'
    criar_novo_usuario(role)

elif d1 == '3':
    programa_encerrado()
    
else:
    print("Opção inválida")
