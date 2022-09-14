from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarcha, bagageiro, velocidade = 0):
        super().__init__(marca, qtdRodas, modelo, velocidade)
        self.numMarcha = numMarcha
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f"""
        Marcha: {self.numMarcha}
        Bagageiro: {self.bagageiro}""")