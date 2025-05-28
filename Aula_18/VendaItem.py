class VendaItem:
    def __init__(self, id, q, p):
        self.setId(id)
        self.setQ(q)
        self.setP(p)
        self.__IdVenda = 0;
        self.__IdProduto = 0;

    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id

    def setQ(self, q):
        self.__q = q
    def getQ(self):
        return self.__q

    def setP(self, p):
        self.__p = p
    def getP(self):
        return self.__p
    
    def setIdVenda(self, id):
        if(id < 0):
            raise ValueError("Valor inválido! Deve ser maior que zero")
        self.__IdVenda = id

    def getIdVenda(self):
        return self.__IdVenda
    
    def setIdProduto(self, id):
        self.__IdProduto = id

    def getIdProduto(self):
        return self.__IdProduto
    
    def __str__(self):
        return f"Id = {self.__id} Quantidade = {self.__q} Preço = {self.__p}"