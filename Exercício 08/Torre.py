class Torre:  
    def __init__(self, id = None, nome = None, endereco = None):
        self.id = id
        self.nome = nome
        self.endereco = endereco
    
    def cadastrar(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def imprimir(self):
        print(f"""
        ID Torre: {self.id}
        Nome Torre: {self.nome}
        Endereço Torre: {self.endereco}        
        """)
