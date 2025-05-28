class Categoria:
    def __init__(self, id, d):
        self.setId(id)
        self.setD(d)

    def setId(self, id):
        self.__id == id

    def getId(self):
        return self.__id
    
    def setD(self,d):
        self.__d == d

    def getD(self):
        return self.__id
    
    def __str__(self):
        return f"Id = {self.__id}  Descrição = {self.__d}"
    