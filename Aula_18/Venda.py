import datetime

class Venda:
    def __init__(self, id):
        self.setId(id)
        self.__Data = datetime.datetime.now()
        self.__Carrinho = True
        self.__total = 0
        self.__idCliente = 0
        

    
    def setId(self,id):
        if(id < 0):
            raise ValueError("Valor Inválido")
        self.__id = id;

    def getId(self):
        return self.__id
    
    def setData(self, data):
        if (data > datetime.datetime.now() or type(data) != datetime):
            raise ValueError("Valor Inválido! Deve ser Datatime")
        self.__Data = data

    def getData(self):
        return self.__Data
    
    def setCarrinho(self, value):
        if (type(value) != bool):
            raise ValueError("Valor Inválido! Deve ser Booleano")
        self.__Carrinho = value

    def getCarrinho(self):
        return self.__Carrinho

    def setTotal(self, total):
        if(total < 0):
            raise ValueError("Valor inválido!")
        self.__total = total

    def getTotal(self):
        return self.__total


    def setIdCliente(self, id):
        if(id < 0):
            raise ValueError("Valor Inválido! Deve ser maior que zero")
        self.__idCliente = id

    def getIdCliente(self):
        return self.__idCliente

    def __str__(self):
        return f"Id = {self.__id} Data = {self.__Data} Carrinho = {self.__Carrinho} Total = {self.__total} Id Cliente = {self.__idCliente} "