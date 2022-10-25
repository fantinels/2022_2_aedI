from Carro import Carro

class FilaLavagem:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self):
        placa = input('Digite a placa do seu carro: ')
        km = input('Digite quantos km tem seu carro: ')
        carro = Carro(placa, km)

        if self.inicio is None:
            self.inicio = carro
            self.fim = carro
        else:
            self.fim.proximo = carro
            self.fim = carro
        
        self.imprimir()
    
    def remover(self):
        if self.inicio is None:
            print('Sem carros na lavagem\n')
        else:
            if self.inicio.proximo is None:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.inicio.proximo
            self.imprimir()
    
    def imprimir(self):
        if self.inicio is None:
            print('Sem carros na lavagem\n')
        else:
            print('----------------------\n')
            texto = ""
            auxiliar = self.inicio
            while (auxiliar):
                texto += "Placa: " + auxiliar.placa + " - " + "KM: " + auxiliar.km + " - "
                auxiliar = auxiliar.proximo
            print(texto)