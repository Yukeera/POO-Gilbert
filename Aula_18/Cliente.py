class Cliente:
    def __init__(self, id, nome, email, fone):
        self.setId(id)
        self.setNome(nome)
        self.setEmail(email)
        self.setFone(fone)

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setFone(self, fone):
        self.__fone = fone
        
    def getFone(self):
        return self.__fone
    
    def __str__(self):
        return f"Id = {self.__id} Nome = {self.__nome} Email = {self.__email} Telefone = {self.__fone}"
    
    