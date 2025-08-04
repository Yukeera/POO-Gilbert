import json
from Models.usuario import Usuario
from Models.modelo import Modelo

class Cliente(Usuario):   # Domínio - Entidades - Várias instâncias
    def __init__(self, id, nome, email, senha, fone):
        self.setId(id)      # atributo da instância
        self.setNome(nome)
        self.setEmail(email)
        self.setSenha(senha)
        self.setFone(fone)
    def __str__(self):
        return f"{self.getId()} - {self.getNome()} - {self.getEmail()} - {self.getFone()}"

    def getFone(self):
        return self.__fone
    
    def setFone(self, fone):
        if (fone == "" or fone is None):
            raise ValueError("O telefone não pode ser vazio.")
        self.__fone = fone

class Clientes(Modelo):    # Persistência - Armazena os objetos em um arquivo/banco de dados
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:     
            with open("clientes.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Cliente(dic["_Usuario__id"], dic["_Usuario__nome"], dic["_Usuario__email"], dic["_Usuario__senha"], dic["_Cliente__fone"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)