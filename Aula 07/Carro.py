from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo = None, ano = None, portas = None):
        super().__init__(modelo, ano)
        self.portas = portas
        print('Carro construído')

    def imprimirEspecifico(self):
        super().imprimir()
        print(f'Portas: {self.portas}')