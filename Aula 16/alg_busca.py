def buscaSeq(v, value):
    found = False
    count = 0
    for valor in v:
        v.sort()
        count += 1
        if valor == value:
            found = True
            print(f"Valor: {value} - Posição: {v.index(value)} - Iterações: {count}")
    if found ==  False:
        print(f"O valor {value} não existe no vetor - foram feitas {count} Iterações para confirmar!")


def buscaBin(v, value):
    found = False
    count = 0
    inicio = 0
    centro = 0
    fim = len(v) - 1

    while (inicio <= fim):
        v.sort()
        count += 1
        centro = inicio + (fim - inicio) // 2
        if value == v[centro]:
            found = True
            print(f"Valor: {value} - Posição: {v.index(value)} - Iterações: {count}")
            break
        else:
            if value > v[centro]:
                inicio = centro + 1
            else:
                fim = centro - 1

    if found == False:
        print(f"O valor {value} não existe no vetor - foram feitas {count} iterações para confirmar!")


def menu():
    while True:
        print("\n")
        print('''=-=-=-=-=-=-=-=-=-=-=-=-
=- ALGORITMO DE BUSCA =-
=-=-=-=-=-=-=-=-=-=-=-=-
=- 1 BUSCA SEQUENCIAL =-
=- 2 BUSCA BINÁRIA -=-=-
=- 3 BUSCA SEQ/BIN -=-=-
=-=-=-=- 0 SAIR =-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-
''')
        opcao = str(input("Digite a opção! [0] - Para sair: "))
        print("\n")
        if opcao == '0':
            break
        elif opcao == '1':
            num = int(input("Digite um valor para Busca Sequêncial: "))
            buscaSeq(v, num)
        elif opcao == '2':
            num = int(input("Digite um valor para Busca Binária: "))
            buscaBin(v, num)
        elif opcao == '3':
            num = int(input("Digite um valor para Busca Sequêncial/Binária: "))
            print('SEQUÊNCIAL:')
            buscaSeq(v, num)
            print('=-=-=-=-=-=-=-=-=-=-=-=-')
            print('BINÁRIA:')
            buscaBin(v, num)
            print('=-=-=-=-=-=-=-=-=-=-=-=-')
        else:
            print('Opção inválida!')
            print("\n")
        menu()
    print('FIM')


#####################      ÍNICIO       #####################

v = [7, 5, 3, 8, 9, 15, 2, 6, 1, 12, 4, 10, 11, 13, 14, 16, 19, 17, 20, 18]
menu()