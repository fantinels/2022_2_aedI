from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, partidaElet, velocidade=0):
        super().__init__(marca, qtdRodas, modelo, potenciaDoMotor, velocidade)
        self.partidaElet = partidaElet

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f"""
        Partida Elétrica: {self.partidaElet}""")