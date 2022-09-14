from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, qtdePortas, velocidade=0):
        super().__init__(marca, qtdRodas, modelo, potenciaDoMotor, velocidade)
        self.qtdePortas = qtdePortas

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f"""
        Qtde de Portas: {self.qtdePortas}""")