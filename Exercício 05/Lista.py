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
