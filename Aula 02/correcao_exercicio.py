produtos = ["Coca-Cola", "Pepsi", "Cheetos"]
preco = [7.79, 5.99, 3.58]
qtds = [100, 50, 75]

def imprimir(posicao):
    print("Nome: ", produtos[posicao])
    print("Preço: ", preco[posicao])
    print("Quantidade: ", qtds[posicao])

def imprimir_todos():
    for i in range( len(produtos) ):
        print("Nome: ", produtos[i])
        print("Preço: ", preco[i])
        print("Quantidade: ", qtds[i])
        print("------------------")

def remover(posicao):
    produtos.pop(posicao)
    preco.pop(posicao)
    qtds.pop(posicao)
    imprimir_todos()

print("1- Imprimir um produto da lista")
print("2- Excluir um produto da lista")

opcao = int(input("Digite sua opção: "))
posicao = int(input("Digite a posição: "))

if opcao == 1:
    imprimir(posicao)
elif opcao == 2:
    remover(posicao)
else:
    imprimir_todos()