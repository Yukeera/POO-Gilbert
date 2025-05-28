class Produto:
    def __init__(self, id, d, p, e):
        self.setId(id)
        self.setDescricao(d)
        self.setPreco(p)
        self.setEstoque(e)
        self.__idCategoria = 0

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setDescricao(self, d):
        self.__d = d
        
    def getDescricao(self):
        return self.__d

    def setPreco(self, p):
        self.__p = p
    def getP(self):
        return self.__p

    def setEstoque(self, qtd):
        if (qtd < 0):
            raise ValueError("Valor Inválido! Deve ser maior que zero!")
        self.__e = qtd

    def getEstoque(self):
        return self.__e
    
    def setIdCategoria(self, id):
        if (id < 0):
            raise ValueError("Valor Inválido!")
        self.__idCategoria = id

    def getIdCategoria(self):
        return self.__idCategoria
    
    def __str__(self):
        return f"Id = {self.__id}  Descrição = {self.__d} Preço = {self.__p} Estoque = {self.__e} "
