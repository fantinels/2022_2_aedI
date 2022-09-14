class Pessoa:
    def __init__(self, codigo, nome, endereco, telefones):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefones = telefones

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, cod):
        self.__codigo = cod
        
    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getEndereco(self):
        return self._endereco

    def setEndereco(self, end):
        self._endereco = end

    def getTelefones(self):
        return self.__telefones

    def setTelefones(self, tel):
        self.__telefones = tel

    """
    -- Não entendi métodos privados
    def __imprimirFone(self):
        print(f"Telefone: {self.__telefones}")
    """
    

    def imprimirNome(self):
        print(f"Código: {self.__codigo}\nNome: {self.nome}\nEndereço: {self._endereco}\nFones: {self.__telefones}")

    


    


        