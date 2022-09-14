class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade = 0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self, velocidadeAtual):
        self.velocidade += velocidadeAtual  

    def frear(self, velocidadeAtual):
        self.velocidade -= velocidadeAtual  

    def imprimirInformacoes(self):
        print(f"""
        Marca: {self.marca}
        Qtd Rodas: {self.qtdRodas}
        Modelo: {self.modelo}
        Velocidade: {self.velocidade}""")