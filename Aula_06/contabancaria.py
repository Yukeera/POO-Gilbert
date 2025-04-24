class ContaBancaria:
    def _init__(self):
        self.__titular = ""
        self.__numero = ""
        self.__saldo = 0
    
def set_titular(self, titular):
        if (titular) == "":
            raise ValueError("O titular não pode ser vazio")
        self.__titular = titular

def get_titular(self):
        return self.__titular

def set_numero(self, numero):
        if (numero) == "":
            raise ValueError("O número não pode ser vazio")
        self.__numero = numero

def get_numero(self):
        return self.__numero

def get_saldo(self):
        return self.__saldo

def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero")
        self.__saldo += valor
        
def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= valor

def menu():
        print("Escolha uma opção:")
        print("1 - Abrir conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Ver saldo")
        return int(input())