from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefones, cnpj, inscricaoEstadual, qtdeFuncionarios):
        super().__init__(codigo, nome, endereco, telefones)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.qtdeFuncionarios = qtdeFuncionarios

    def getCnpj(self):
        return self.__cnpj

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    def getInscricaoEstad(self):
        return self.__inscricaoEstadual

    def setInscricaoEstad(self, inscricao):
        self.__inscricaoEstadual = inscricao

    def getQtdFunc(self):
        return self.qtdeFuncionarios

    def setQtdFunc(self, qtde):
        self.qtdeFuncionarios = qtde

    def emitirNF(self):
        return f"""
        --- NOTA FISCAL ---
        Nome da Empresa: {self.nome}
        Endereço da Empresa: {self._endereco}
        N° Inscrição Estadual: {self.__inscricaoEstadual}
        CNPJ da Empresa: {self.__cnpj}
        """

    def imprimirCnpj(self):
        super().imprimirNome()
        print(f"CNPJ da Empresa: {self.__cnpj}\nN° Insc. Estad.: {self.__inscricaoEstadual}\nQtde Funcionários: {self.qtdeFuncionarios}\n{self.emitirNF()}")