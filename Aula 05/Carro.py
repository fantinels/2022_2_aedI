from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo = "Fusca", qtdePortas = 4):
        super().__init__(modelo)
        self.qtdePortas = qtdePortas

    def imprimir(self):
        super().imprimir()
        print(f"Qtde de portas: {self.qtdePortas}")

    def __str__(self) -> str:
        return super().__str__() + "\nQtde de portas: " + str(self.qtdePortas)