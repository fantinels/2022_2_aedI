class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def imprimir(self):
        print(self.marca, self.ano)