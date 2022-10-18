from No import No


class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
            self.fim = nodo
            return

        # Adicionando na última posição
        self.fim.proximo = nodo
        nodo.anterior = self.fim
        self.fim = nodo

        self.imprimir()

    # Trocar de valor (anterior e próximo)
    def trocaValor(self, primeiro, segundo):
        valor = primeiro.dado
        primeiro.dado = segundo.dado
        segundo.dado = valor


    def adicionarOrdem(self):
        if self.inicio == None:
             return
        
        task = True
        # Pegando o primeiro nodo
        comeco = self.inicio
        while (task == True):
            task = False
            while (comeco != None and comeco.proximo != None):
                if comeco.dado > comeco.proximo.dado:
                    self.trocaValor(comeco, comeco.proximo)
                    # Ativando a próxima iteração
                    task = True
                
                comeco = comeco.proximo
            
        comeco = self.inicio

        self.imprimir()

    def remover(self, valorDel):
        if self.inicio == None:
            print('Lista vazia\n----------------------')
            return
        if self.inicio.proximo == None:
            if self.inicio.dado == valorDel:
                self.inicio = None
            else:
                print('Valor não encontrado\n----------------------')
            return
        if self.inicio.dado == valorDel:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
            return
        
        aux = self.inicio
        while aux.proximo != None:
            if aux.dado == valorDel:
                break
            aux = aux.proximo
        if aux.proximo != None:
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
        else:
            if aux.dado == valorDel:
                aux.anterior.proximo = None
            else:
                print('Valor não encontrado\n----------------------')
        
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print('Lista vazia\n----------------------')
        else:
            print('----------------------\n', '\nLista - Ínicio ao fim')
            auxiliar = self.inicio
            while (auxiliar != None):
                print(auxiliar.dado, '\n')
                auxiliar = auxiliar.proximo

            print('----------------------\n', '\nLista - Fim ao íncio')
            auxiliar = self.fim
            while (auxiliar != None):
                print(auxiliar.dado, '\n')
                auxiliar = auxiliar.anterior
