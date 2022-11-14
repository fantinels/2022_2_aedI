from Apartamento import Apartamento

class FilaEspera():
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def adicionarApe(self, ape):
        if self.inicio == None:
            self.inicio = ape
            self.fim = ape
        else:
            self.fim.proximo = ape
            self.fim = ape
        
        self.imprimir()

    def remover(self, vaga):
        if self.inicio == None:
            print('Fila vazia!')
        else:
            if self.inicio.proximo == None:
                self.inicio.vaga = vaga
                self.inicio = None
                self.fim = None
            else:
                self.inicio.vaga = vaga
                self.inicio = self.inicio.proximo
    
    def imprimir(self):
        if self.inicio == None:
            print('Fila vazia!')
        else:
            print('--------------\n')
            print("Apartamentos na fila de espera:\n")
            aux = self.inicio
            while aux:
                aux.imprimirApe()
                aux = aux.proximo
            print('Fim da fila de espera!')