from calendar import c
from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefones, cpf, idade, peso, altura):
        super().__init__(codigo, nome, endereco, telefones)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def getCpf(self):
        return self.__cpf

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade

    def calculaImc(self):
        imc = self.peso / self.altura ** 2
        return f"O IMC de {self.peso} kg é de {round(imc)}"

    def imprimirCpf(self):
        super().imprimirNome()
        print(f"CPF: {self.__cpf}\nIdade: {self.idade}\nPeso (kg): {self.peso}\nAltura: {self.altura}\n{self.calculaImc()}")