class Endereco:
    def __init__(self, logradouro, cidade):
        self.id = None
        self.logradouro = logradouro
        self.cidade = cidade

    def imprimir(self):
        print(f"Logradouro: {self.logradouro}")
        print(f"Cidade: {self.cidade.nome}")