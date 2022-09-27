from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo = None, cor = None, preco = None, potenciaDaFonte = None):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    @property
    def potencia(self):
        return self._potenciaDaFonte

    @potencia.setter
    def potencia(self, valor):
        self._potenciaDaFonte = valor

    def cadastrar(self, modelo, cor, preco, potenciaDaFonte):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return super().getInformacoes() + f"""\nPotência da Fonte: {self._potenciaDaFonte}"""

    