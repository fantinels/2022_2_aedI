from Livro import Livro

class Pilha:
    def __init__(self):
        self.topo = None

    def adicionar(self, nome):
        livro = Livro(nome)
        
        if self.topo == None:
            self.topo = livro
        else:
            livro.proximo = self.topo
            self.topo = livro

        self.imprimir()
    
    def remover(self):
        if self.topo == None:
            print('Pilha vazia!\n')
        else:
            print('----------------------\n')
            self.topo = self.topo.proximo

        self.imprimir()
    
    def imprimir(self):
        if self.topo == None:
            print('Pilha vazia!\n')
        else:
            print('----------------------\n')
            auxiliar = self.topo
            while (auxiliar):
                print(auxiliar.nome, "\n")
                auxiliar = auxiliar.proximo