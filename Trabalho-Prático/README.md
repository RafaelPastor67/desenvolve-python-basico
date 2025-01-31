# Sistema de Gerenciamento de Usuários e Produtos

Este projeto simula uma empresa fictícia que opera como uma loja de periféricos eletrônicos. Ao executar o código, o usuário poderá escolher entre **fazer login** ou **criar uma conta**.

## Funcionalidades

- **Cadastro e Login**:
  - Ao criar uma conta, o cargo do usuário será **Cliente** por padrão.
  - Clientes têm permissão apenas para visualizar o catálogo de produtos.

- **Níveis de Acesso**:
  - O arquivo `user.csv` já contém alguns usuários pré-cadastrados com diferentes cargos.
  - **Funcionários ("employer")**:
    - Podem visualizar o catálogo de produtos.
    - Têm permissão para **adicionar, remover e editar produtos**.
  - **Administradores ("Admin")**:
    - Possuem todas as permissões dos funcionários.
    - Podem **visualizar, excluir, editar e criar novos usuários**, atribuindo cargos diferentes dentro da empresa.

## Estrutura de Dados

- **Usuários** são armazenados no arquivo `user.csv`.
- **Produtos** podem ser adicionados, removidos e editados através do sistema.