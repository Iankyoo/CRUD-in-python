import os

estoque = []
contador_id = 1

def exibir_sub_titulo(texto):
    """
    Limpa o terminal e exibe um título formatado com bordas.

    Parâmetros:
    texto (str): Texto do subtítulo a ser exibido.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)

def voltar_ao_menu():
    """
    Pausa a execução aguardando o usuário pressionar uma tecla.
    """
    input('\nDigite uma tecla para voltar ao menu')
    
def adicionar():
    """
    Adiciona um novo produto ao estoque.

    Solicita nome, preço e quantidade do produto.
    Valida entradas numéricas e incrementa o ID automaticamente.
    """
    global contador_id
    exibir_sub_titulo('ADICIONAR UM NOVO PRODUTO')
    nome = input('Digite o nome do produto: ')

    try:
        preco = float(input('Digite o valor do produto: '))
        quantidade = int(input('Digite a quantidade em estoque: '))

        novo_produto = {
            'id': contador_id,
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }

        estoque.append(novo_produto)
        print(f'O produto {novo_produto} foi adicionado ao estoque com sucesso. (id: {contador_id})')
        contador_id += 1
    except ValueError:
        print('Erro: digite números válidos para o preço e quantidade!')

def listar(pausa=True):
    """
    Lista todos os produtos cadastrados no estoque.

    Parâmetros:
    pausa (bool): Se True, aguarda o usuário antes de retornar ao menu.
    """
    exibir_sub_titulo('LISTA DE PRODUTOS')
    if not estoque:
        print('Nenhum produto cadastrado')
    else:
        print(f"{'Nome'.ljust(22)} | {'Preço'.ljust(20)} | {'Quantidade'.ljust(20)} | Id")
        for produto in estoque:
            print(f"-{produto['nome'].ljust(20)} | R${produto['preco']:<20.2f} | {produto['quantidade']:<20.2f} un.| {produto['id']} ")
    if pausa:
        voltar_ao_menu()

def atualizar():
    """
    Atualiza informações de um produto pelo ID.

    Permite alterar nome, preço ou quantidade do produto selecionado.
    """
    exibir_sub_titulo('ATUALIZANDO PRODUTO')
    listar(pausa=False)

    try:
        id_busca = int(input('\nID do produto para editar: '))
        produto = next((p for p in estoque if p['id'] == id_busca), None)

        if not produto:
            print('Produto não encontrado.')
            return
    
        while True:
            exibir_sub_titulo(f"Editando: {produto['nome']}")
            print(f"1 - Alterar Nome (Atual: {produto['nome']})")
            print(f"2 - Alterar Preço (Atual: {produto['preco']})")
            print(f"3 - Alterar Quantidade (Atual: {produto['quantidade']})")
            print(f"4 - Concluir Edição")
            
            opcao = int(input('O que você deseja alterar?'))

            if opcao == 1:
                novo_nome = input('Novo nome: ').strip()
                produto['nome'] = novo_nome
                print('Nome atualizado!')
            elif opcao == 2:
                novo_preco = float(input('Novo preço: '))
                produto['preco'] = novo_preco
                print('Preço atualizado!')
            elif opcao == 3:
                nova_quantidade = int(input('Nova quantidade: '))
                produto['quantidade'] = nova_quantidade
            elif opcao == 4:
                print('Edição finalizada')
                break
            else:
                print('Opção inválida.')
    except ValueError:
        print('O ID deve ser um número!')

def remover():
    """
    Remove um produto do estoque pelo ID.

    Exibe a lista, solicita o ID e exclui o item correspondente.
    """
    exibir_sub_titulo('REMOVER UM PRODUTO')
    listar(pausa=False)

    try:
        id_busca = int(input('\nDigite o ID do produto que deseja excluir'))
        produto = next((p for p in estoque if p['id'] == id_busca), None)
        if produto:
            estoque.remove(produto)
            print('Produto removido!')
        else:
            print('O produto com este ID não foi encontrado!')

    except ValueError:
        print('O ID deve ser um número!')

def menu():
    """
    Exibe o menu principal do sistema e direciona para as funções.

    Garante tratamento de erros para entradas inválidas.
    """
    while True:
        exibir_sub_titulo('GESTÃO DE ESTOQUE')
        print('1 - Adicionar produto')
        print('2 - Listar produtos')
        print('3 - Atualizar produto')
        print('4 - Remover produto')
        print('5 - Sair')

        try: 
            opcao = int(input('\nDigite a opção desejada: '))
            if opcao == 1:
                adicionar()
            elif opcao == 2:
                listar()
            elif opcao == 3:
                atualizar()
            elif opcao == 4:
                remover()
            elif opcao == 5:
                print('Finalizando o programa...')
                break
            else:
                print('Opção inválida!')
        except ValueError:
            print('Erro: Digite uma opção válida')

def main():
    """
    Função principal que inicia o programa.

    Responsável apenas por chamar o menu.
    """
    menu()

if __name__ == '__main__':
    main()
