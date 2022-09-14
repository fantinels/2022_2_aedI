# def getPi():
#    return 3.14


# def imprimePi():
#    print( getPi() )


# def calculaAreaCirculo(raio):
#    return getPi() * ( raio * raio )

# def imprimeAreaCirculo(raio):
#    print( calculaAreaCirculo(raio) )

# imprimeAreaCirculo(3)

#############################################

# carros = ["Uno", "Doblo", "Toro", "500", "147"]

# print(carros)

# print(carros[2])

# print(carros[2:])

#############################################

"""
• Construir um algoritmo que contenha 3 listas, cada lista contendo:
• Nomes de produtos
• Preços de cada produto
• Quantidades de cada produto
• Construir uma função para imprimir um dos produtos da lista e uma
função para retirar um dos produtos das listas. As funções devem receber
um parâmetro que será usado para acessar a posição dos itens das listas
que serão impressos ou retirados.

"""

nome_produto = ["Pastel", "Bolo", "Donuts"]
preco_produto = [5.0, 3.50, 7.00]
qtd_produto = [6, 4, 10]

def ImprimeProduto(index):
    print(f"Produto: {nome_produto[index]} - Preço: {preco_produto[index]} - Quantidade: {qtd_produto[index]}")

def RemoveProduto(index):
    print(f"Listas antes de terem itens removidos: Produto: {nome_produto} - Preço: {preco_produto} - Quantidade: {qtd_produto}")
    nome_produto.pop(index)
    preco_produto.pop(index)
    qtd_produto.pop(index)
    print(f"Listas depois de terem um item removido: Produto: {nome_produto} - Preço: {preco_produto} - Quantidade: {qtd_produto}")

ImprimeProduto(1)
RemoveProduto(2)


