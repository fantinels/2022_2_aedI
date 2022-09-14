from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marcaMoto, anoMoto, partidaElet):
        super().__init__(marcaMoto, anoMoto)
        self.partidaElet = partidaElet
        print('Moto construída')