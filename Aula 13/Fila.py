from Carro import Carro

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, placa, km):
        carro = Carro(placa, km)
        if(self.inicio == None):
            self.inicio = carro
            self.fim = carro
        else:
            self.fim.proximo = carro
            self.fim = carro
        self.imprimir()
    
    def imprimir(self):
        if self.inicio == None:
            print("Nenhum carro na fila!\n-----------")
        else:
            print("-----------\n")
            texto = ""
            aux = self.inicio
            while aux:
                texto += "Placa: " + aux.placa + " / KM: " + str(aux.km) + " - "
                aux = aux.proximo
            print(texto)

    def remover(self):
        if self.inicio == None:
            print("Nenhum carro na fila!\n-----------")
        else:
            if self.inicio.proximo == None:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.inicio.proximo
            self.imprimir()