from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marcaCar, anoCar, qtdPortas):
        super().__init__(marcaCar, anoCar)
        self.qtdPortas = qtdPortas
        print('Carro construído')