import datetime

class atleta:
    def __init__(self, id, nome, nascimento):
        self.__id = id
        self.__nome = nome
        self.__nascimento = nascimento

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if (id <= 0):
            raise ValueError("O valor tem que ser maior que zero")
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if(type(nome) != 'str' or nome == ""):
            raise ValueError("O nome precisa ser um texto com mais de 1 character")
        self.__nome = nome

    @property
    def nascimento (self):
        return self.__nascimento

    def __str__(self):
        return f"Id ={self.__id} Nome = {self.__nome}  Nascimento {self.__nascimento}"