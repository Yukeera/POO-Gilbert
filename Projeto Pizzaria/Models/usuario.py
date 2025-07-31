from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self, id, nome, email, senha):
        self.setId(id)      # atributo da instância
        self.setNome(nome)
        self.setEmail(email)
        self.setSenha(senha)
        self.__admin = False  # Indica se o usuário é um administrador
        
    def __str__(self):
        return f"{self.getId()} - {self.getNome()} - {self.getEmail()}"

    def getId(self):
        return self.__id
    
    def setId(self, id):
        if (id < 0):
            raise ValueError("O ID não pode ser negativo.")
        self.__id = id

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        if (nome == "" or nome is None):
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = nome

    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        if (email == "" or email is None):
            raise ValueError("O email não pode ser vazio.")
        self.__email = email

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha):
        if (senha == "" or senha is None):
            raise ValueError("A senha não pode ser vazia.")
        self.__senha = senha

    def getAdmin(self):
        return self.__admin
    
    def setAdmin(self, admin):
        if not isinstance(admin, bool):
            raise ValueError("O valor de admin deve ser booleano.")
        self.__admin = admin