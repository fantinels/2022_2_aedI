from No import No

class Lista:
    def __init__(self):
        self.inicio = None

    def adicionarNoFim(self, valor):
        nodo = No(valor)

        if self.inicio == None:
            self.inicio = nodo
        else:
            auxiliar = self.inicio
            # Percorre a lista para chegar no último elemento
            while (auxiliar.proximo):
                auxiliar = auxiliar.proximo

            auxiliar.proximo = nodo

        self.imprimir()

    def adicionarNoInicio(self, valor):
        nodo = No(valor)

        if self.inicio == None:
            self.inicio = nodo
        else:
            nodo.proximo = self.inicio
            self.inicio = nodo

        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print('Lista vazia\n----------------------')
        else:
            print('----------------------\n')
            auxiliar = self.inicio
            while (auxiliar):
                print(auxiliar.dado, '\n')
                auxiliar = auxiliar.proximo

    def removerDoInicio(self):
        if self.inicio == None:
            print('Lista vazia\n----------------------')
        elif self.inicio.proximo == None:
            self.inicio = None
        else:
            self.inicio = self.inicio.proximo

        self.imprimir()

    def removerDoFim(self):
        if self.inicio == None:
            print('Lista vazia\n----------------------')
        elif self.inicio.proximo == None:
            self.inicio = None
        else:
            anterior = self.inicio
            auxiliar = self.inicio.proximo
            # Percorre a lista para chegar no último elemento
            while (auxiliar.proximo):
                anterior = auxiliar
                auxiliar = auxiliar.proximo
            anterior.proximo = None

        self.imprimir()

