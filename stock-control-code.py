#Ao iniciar a sessão
def introducao():
  '''
    Exibe o menu de opções para o sistema de estoque.
  '''
  print('''
      1 - Cadastro de produto
      2 - Listagem de produto
      3 - Ordenar produto por quantidade
      4 - Buscar produto
      5 - Remover produto
      6 - Consultar produtos esgotados
      7 - Filtrar produtos de baixa quantidade
      8 - Atualizar produto
      9 - Calcular o valor total do estoque
      10 - Calcular o lucro presumido do estoque
      11 - Gerar relatório geral do estoque
  ''')

#Finalizar sessão
def finalizar():
  '''
    Pergunta ao usuário se deseja finalizar a sessão. Retorna True se a resposta for "não", caso contrário retorna False.
  '''
  resposta = input('Deseja executar outra ação? ')
  if resposta.lower() in ('n', 'nao', 'não'):
    return True
  return False


#Cadastramento de produto
def cadastro_produto():
    '''
      Realiza o cadastramento de novos produtos no estoque. Pede detalhes como nome, código, quantidade, custo e preço.
      Retorna o estoque atualizado com o novo produto.
    '''
    global estoque_inicial

    #Detalhamento do produto
    produtos = ""
    while(True):
      descricao = input('Digite o nome do produto: ')
      codigo = int(input('Digite o código do produto: '))
      quantitadeEstoque = int(input('Digite a quantidade em estoque: '))
      custoItem = float(input('Digite o custo do produto: '))
      precoVenda = float(input('Digite o valor da venda: '))

      estoque_inicial += f"#{descricao};{codigo};{quantitadeEstoque};{custoItem};{precoVenda}"

      #Verificar se o usuário deseja cadastrar mais um produto
      resposta = input("Deseja cadastrar mais um produto? ")
      if resposta.lower() in ('n', 'nao', 'não'):
        break

    return estoque_inicial

#Listagem de todos os produtos cadastrados
def listagem_produtos():
  '''
    Exibe a listagem de todos os produtos cadastrados no estoque, mostrando a descrição, código, quantidade, custo e preço de venda.
  '''
  #Separação de produtos usando split()
  lista_produtos = estoque_inicial.split('#')
  #Listando todos os produtos
  for produto in lista_produtos:
    atributos = produto.split(';')
    print(f'Descrição: {atributos[0]}, Código:  {atributos[1]}, Quantidade:{atributos[2]}, Custo do item: {atributos[3]}, Preço de venda: {atributos[4]}')

#Ordenação de produtos por quantidade
def ordenar_produtos_quantidade(ordem='crescente'):
    '''
    Função que ordena os produtos do estoque pela quantidade.
    
    Params:
    ordem (str): Define a ordem da listagem, pode ser 'crescente' ou 'decrescente'.
    '''
    #Separação de produtos usando split()
    produtos = estoque_inicial.split('#')
    #Obtenção dos atributos de cada produto
    lista_produtos = []
    for produto in produtos:
      atributos = produto.split(';')
      descricao = atributos[0]
      codigo = atributos[1]
      quantidade = atributos[2]
      custoItem = atributos[3]
      precoVenda = atributos[4]
      lista_produtos.append([descricao,codigo,quantidade,custoItem,precoVenda])

    #Verifica qual a ordem desejada pelo usuário
    if ordem.lower() == 'decrescente':
      lista_produtos.sort(key=lambda x: x[2], reverse=True)
    else:
      lista_produtos.sort(key=lambda x: x[2])
    for produto in lista_produtos:
      print(f'Descrição: {produto[0]}, Código:  {produto[1]}, Quantidade:{produto[2]}, Custo do item: {produto[3]}, Preço de venda: {produto[4]}')

#Busca de produto com base na descricao ou código
def buscar_produto():
  '''
    Função para buscar produtos no estoque com base na descrição ou código.
    Pergunta ao usuário pelo filtro desejado (descrição ou código) e exibe os resultados encontrados.
  '''
  #Separação de produtos usando split()
  produtos = estoque_inicial.split('#')
  #Obtenção dos atributos de cada produto
  lista_produtos = [produto.split(';') for produto in produtos]

  #Verifica o filtro desejado pelo usuário
  filtro = input("Pelo que você deseja filtrar? (descricao ou código) ")
  if filtro.lower() in ('descrição','descricao'):
    alvo = input("Digite a descrição do produto")
    produtos_encontrados = [produto for produto in lista_produtos if alvo in produto[0]]
    #Listagem de produtos pelo descrição
    for produto in produtos_encontrados:
      print(produto)
  else:
    alvo = input("Digite a código do produto")
    produtos_encontrados = [produto for produto in lista_produtos if alvo in produto[1]]
    #Listagem de produtos pelo código
    for produto in produtos_encontrados:
      print(produto)

#Remover produto do estoque
def remover_produto():
    '''
      Função que remove ou ajusta a quantidade de um produto no estoque.
      O usuário pode remover completamente um produto ou reduzir a quantidade em estoque.
    '''
    global estoque_inicial
    # Separação de produtos usando split()
    produtos = estoque_inicial.split('#')
    #Listagem de produtos para o usuário saber qual o código desejado para remoção
    listagem_produtos()

    # Obtenção dos atributos de cada produto
    lista_produtos = [produto.split(';') for produto in produtos]
    code = input('Digite o código do produto: ')

    # Compressão de lista para encontrar o produto
    produto_encontrado = next((produto for produto in lista_produtos if produto[1] == code), None)

    if produto_encontrado:
        print(f'Produto encontrado: {produto_encontrado}')
        # Pedindo a quantidade que o usuário deseja remover
        quantidade_remover = int(input('Digite a quantidade a remover: '))
        # Verificando a quantidade atual
        quantidade_atual = int(produto_encontrado[2])

        if quantidade_remover >= quantidade_atual:
            # Se a quantidade a remover for maior ou igual, removemos o produto inteiro
            lista_produtos.remove(produto_encontrado)
            print('Produto removido completamente!')
        else:
            # Senão, apenas subtraímos a quantidade
            produto_encontrado[2] = str(quantidade_atual - quantidade_remover)
            print(f'Nova quantidade do produto {produto_encontrado[0]}: {produto_encontrado[2]}')

        # Atualizando a string estoque_inicial com os produtos restantes
        estoque_inicial = '#'.join([';'.join(produto) for produto in lista_produtos])

        print('Novo estoque: ')
        listagem_produtos()
    else:
        print('Produto não encontrado.')

#Consultar produtos esgotados
def consultar_produto_esgotado():
    '''
    Função que consulta produtos esgotados no estoque (com quantidade igual a 0).
    Exibe a lista de produtos esgotados com seus respectivos atributos.
    '''
    # Separação de produtos usando split()
    produtos = estoque_inicial.split('#')
    # Obtenção dos atributos de cada produto
    lista_produtos = [produto.split(';') for produto in produtos]

    # Compressão de lista para encontrar o produto
    # produto[0] = Descricao
    # produto[1] = Codigo
    # produto[2] = Quantidade
    # produto[3] = Custo do item
    # produto[4] = Preco de venda
    produto_esgotados = [produto for produto in lista_produtos if produto[2] == '0']
    produtos =  '#'.join([';'.join(produto) for produto in produto_esgotados])
    if produto_esgotados:
        # Concatena os atributos do produto encontrado em uma string
        for produto in produto_esgotados:
            print(f'Descrição: {produto[0]}, Código: {produto[1]}, Quantidade: {produto[2]}, Custo do item: {produto[3]}, Preço de venda: {produto[4]}')
    else:
        print("Nenhum produto esgotado encontrado.")

#Filtragem por baixa quantidade
def filtrar_baixa_quantaide(limite_minimo=5):
  '''
    Filtra os produtos que possuem quantidade abaixo do limite mínimo.
    
    Params:
    limite_minimo (int): Quantidade mínima para considerar um produto em baixa quantidade. O valor padrão é 5.

    A função percorre a lista de produtos no estoque, separa aqueles cuja quantidade está abaixo do limite especificado e os exibe com seus respectivos detalhes (descrição, código, quantidade, custo e preço de venda).
  '''
  # Separação de produtos usando split()
  produtos = estoque_inicial.split('#')
  # Inicialização da lista
  produtos_baixa_quantidade = []

  # Preenchimento da lista de baixa quantidade
  for produto in produtos:
      lista_produtos = produto.split(';')
      if int(lista_produtos[2]) < limite_minimo:
          produtos_baixa_quantidade.append(produto)
  # Listagem da lista de produtos em baixa quantidade
  for produto in produtos_baixa_quantidade:
    atributo = produto.split(';')
    print(f'Descrição: {atributo[0]}, Código: {atributo[1]}, Quantidade: {atributo[2]}, Custo do item: {atributo[3]}, Preço de venda: {atributo[4]}')

#Validação de atualização
def validar_atualizacao(atributos, nova_quantidade=None, novo_preco=None):
    """
    Valida se a nova quantidade e preço são válidos.

    :param atributos: Lista de atributos do produto.
    :param nova_quantidade: Nova quantidade para validar.
    :param novo_preco: Novo preço de venda para validar.
    :return: True se a validação passar, False caso contrário.
    """
    quantidade_atual = int(atributos[2])  # Atributo de quantidade atual
    custo_atual = float(atributos[3])      # Atributo de custo atual

    if nova_quantidade is not None:
        # Verifica se a nova quantidade não deixa o estoque negativo
        if quantidade_atual + nova_quantidade < 0:
            print("Erro: A nova quantidade não pode deixar o estoque negativo.")
            return False

    if novo_preco is not None:
        # Verifica se o novo preço de venda não é menor que o custo do item
        if novo_preco < custo_atual:
            print("Erro: O preço de venda não pode ser menor que o custo do item.")
            return False

    return True

# Atualização do estoque | Também permite alterar o preço de venda de um produto
def atualizar_estoque():
    '''
      Função que atualiza as informações de um produto no estoque.
      Permite alterar a descrição, código, quantidade, custo e preço de venda do produto.
      O estoque é atualizado dinamicamente após a modificação.
    '''
    global estoque_inicial
    produtos = estoque_inicial.split('#')
    lista_produtos = [produto.split(';') for produto in produtos]
    listagem_produtos()

    alvo = input('Digite o código do produto: ')
    produto_encontrado = [produto for produto in lista_produtos if alvo in produto[1]]

    if not produto_encontrado:
        print("Produto não encontrado.")
        return

    atributos = produto_encontrado[0]
    print(f"Produto encontrado: {atributos}")

    alvo_atualizacao = input('O que você deseja atualizar? (descrição = d, código = c, quantidade = q, custo do item = ci ou preço de venda = pv): ')

    match alvo_atualizacao:
        case 'd':
            nova_descricao = input('Digite a nova descrição: ')
            atributos[0] = nova_descricao
        case 'c':
            novo_codigo = input('Digite o novo código: ')
            atributos[1] = novo_codigo
        case 'q':
            nova_quantidade = int(input('Digite a nova quantidade: '))
            if not validar_atualizacao(atributos, nova_quantidade=nova_quantidade):
                return
            atributos[2] = str(int(atributos[2]) + nova_quantidade) 
        case 'ci':
            novo_custo = input('Digite o novo custo do item: ')
            try:
                novo_custo_float = float(novo_custo)
                atributos[3] = novo_custo_float
            except ValueError:
                print("Custo inválido. Deve ser um número.")
                return
        case 'pv':
            novo_preco = input('Digite o novo preço de venda: ')
            try:
                novo_preco_float = float(novo_preco)
                # Validação do preço
                if not validar_atualizacao(atributos, novo_preco=novo_preco_float):
                    return
                atributos[4] = novo_preco_float
            except ValueError:
                print("Preço inválido. Deve ser um número.")
                return
        case _:
            print("Opção de atualização inválida.")
            return

    # Atualiza a lista de produtos
    lista_produtos[lista_produtos.index(produto_encontrado[0])] = atributos

    # Atualiza o estoque inicial
    estoque_inicial = '#'.join([';'.join(produto) for produto in lista_produtos])

    print("Estoque atualizado com sucesso.")

# Função para processar a string do estoque inicial e convertê-la em uma lista de produtos
def processar_estoque():
    '''
      Converte a string de estoque inicial em uma lista de dicionários de produtos.
      Cada produto contém descrição, código, quantidade, custo e preço de venda.
    '''
    produtos = []
    itens = estoque_inicial.split('#')
    
    for item in itens:
        descricao, codigo, quantidade, custo, preco_venda = item.split(';')
        produtos.append({
            'descricao': descricao,
            'codigo': int(codigo),
            'quantidade': int(quantidade),
            'custo': float(custo),
            'preco_venda': float(preco_venda)
        })
    return produtos

# Função para calcular o valor total do estoque
def calcular_valor_total_estoque(produtos):
    '''
      Calcula o valor total do estoque multiplicando a quantidade pelo preço de venda de cada produto.
      
      :param produtos: Lista de dicionários com as informações dos produtos.
      :return: Valor total do estoque.
    '''
    valor_total = sum(produto['quantidade'] * produto['preco_venda'] for produto in produtos)
    print('Valor total do estoque: ', valor_total)

# Função para calcular o lucro presumido do estoque
def calcular_lucro_presumido(produtos):
    '''
      Calcula o lucro presumido do estoque com base na diferença entre o preço de venda e o custo,
      multiplicado pela quantidade disponível de cada item.
      
      :param produtos: Lista de dicionários com as informações dos produtos.
      :return: Lucro total presumido do estoque.
    '''
    lucro_total = sum((produto['preco_venda'] - produto['custo']) * produto['quantidade'] for produto in produtos)
    print('Lucro presumido do estoque: ', lucro_total)

# Função para gerar um relatório geral do estoque | Feito codigo base, usando GPT para otimizar o codigo
def gerar_relatorio_estoque(produtos):
    '''
      Gera um relatório geral no terminal com a descrição, código, quantidade, custo, preço de venda,
      e o valor total por item (quantidade * preço de venda). Também exibe o custo total e o faturamento total do estoque.
      
      :param produtos: Lista de dicionários com as informações dos produtos.
    '''
    custo_total = 0
    faturamento_total = 0
    
    print(f"{'Descrição'.ljust(30)} {'Código'.rjust(6)} {'Qtd'.rjust(5)} {'Custo'.rjust(10)} {'Preço Venda'.rjust(15)} {'Valor Total'.rjust(15)}")
    print("=" * 90)
    
    for produto in produtos:
        valor_total = produto['quantidade'] * produto['preco_venda']
        custo_total += produto['quantidade'] * produto['custo']
        faturamento_total += valor_total
        
        print(f"{produto['descricao'].ljust(30)} {str(produto['codigo']).rjust(6)} {str(produto['quantidade']).rjust(5)} "
              f"{str(produto['custo']).rjust(10)} {str(produto['preco_venda']).rjust(15)} {str(valor_total).rjust(15)}")
    
    print("=" * 90)
    print(f"Custo Total: {custo_total:.2f}".rjust(70))
    print(f"Faturamento Total: {faturamento_total:.2f}".rjust(70))

estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;0;800.00;1200.00#Monitor LG;206;0;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

#Introdução
def main():
  print('Olá bem-vindo! O que você deseja fazer?')
  introducao()

  produtos = processar_estoque()
  while(True):
    
    opcao = int(input('Digite o numero da ação desejada: '))
  
    if opcao == 1:
        estoque_inicial = cadastro_produto()
    elif opcao == 2:
        listagem_produtos()
    elif opcao == 3:
        ordenar_produtos_quantidade()
    elif opcao == 4:
        buscar_produto()
    elif opcao == 5:
        remover_produto()
    elif opcao == 6:
        consultar_produto_esgotado()
    elif opcao == 7:
        filtrar_baixa_quantaide()
    elif opcao == 8:
        atualizar_estoque()
    elif opcao == 9:
        calcular_valor_total_estoque(produtos)
    elif opcao == 10:
        calcular_lucro_presumido(produtos)
    elif opcao == 11:
        gerar_relatorio_estoque(produtos)
    else:
        print("Opção inválida.")
    
    if finalizar():
        break
    else:
      introducao()

main()
