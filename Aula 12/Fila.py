from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        # self.tamanho = 0

    def adicionar(self, valor):
        no = No(valor)

        if self.inicio is None:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        
        self.imprimir()
    
    def remover(self):
        if self.inicio is None:
            print('Lista vazia\n')
        else:
            if self.inicio.proximo is None:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.inicio.proximo
            self.imprimir()
    
    def imprimir(self):
        if self.inicio is None:
            print('Lista vazia\n')
        else:
            print('----------------------\n')
            texto = ""
            auxiliar = self.inicio
            while (auxiliar):
                texto += auxiliar.dado + " - "
                auxiliar = auxiliar.proximo
            print(texto)