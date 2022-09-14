class Pessoa:
    def __init__(self, nome, fone, endereco):
        self.id = None
        self.nome = nome
        self.fone = fone
        self.end = endereco

    def getCidade(self):
        return self.cidade.nome

    def cadastrar(self):
        print(f"Nome: {self.nome} - Endereço: {self.endereco.imprimir()}")
        
