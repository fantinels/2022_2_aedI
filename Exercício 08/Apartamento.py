from Torre import Torre

class Apartamento:
    def __init__(self, id = None, numero = None, torre = None, vaga = None):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None

    def cadastrar(self, id, numero, torre, vaga = 0):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga

    def imprimirApe(self):
        print(f"""
        --- APARTAMENTO ---
        ID Ape: {self.id}
        Número Ape: {self.numero}
        Vaga: {self.vaga}
        Torre:
        """)
        self.torre.imprimir()