class Conta:
    logado = True
    tarifa = 1.99

    def __init__(self):
        self.__saldo = 0.0

    def __descontarTarifa(self):
        if self.__saldo >= self.tarifa:
            self.__saldo -= self.tarifa
            return True
        else:
            return False        

    def depositar(self, valor):
        if self.__saldo + valor >= self.tarifa:
            self.__saldo += valor
            self.__descontarTarifa()
        else:
            print("Valor insuficiente")

    def sacar(self, valor):
        if valor <= self.__saldo - self.tarifa:
            self.__saldo -+ valor
            self.__descontarTarifa()
        else:
            print("Saldo insuficiente")

    @property
    def saldo(self):
        if self.logado:
            return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if self.logado:
            self.__saldo = saldo

    # Método acessor
    def getSaldo(self):
        if self.logado:
            return self.__saldo
        
    # Método modificador
    def setSaldo(self, novoSaldo):
        if self.logado:
            self.__saldo = novoSaldo