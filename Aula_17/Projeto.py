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
        return f"Id = {self.__id} Nome = {self.__nome}  Email = {self.__email} Fone = {self.__fone}"

class ClientesDAO:
    __objetos = [] # Atributo de class, não pode estar dentro do INIT, pois se o mesmo estiver a class que deve ser estatica vai necessitar ser instaciada

    @classmethod
    def inserir(cls, obj):
        cls.__objetos.append(obj)

    @classmethod
    def listar(cls):
        return cls.__objetos

class UI:
    
    @staticmethod
    def menu():
        print("Cadastro de Clientes")
    
        pass

    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            
        while ()
