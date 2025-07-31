import json
from Models.usuario import Usuario
from Models.modelo import Modelo

class Entregador(Usuario):   # Domínio - Entidades - Várias instâncias
    def __init__(self, id, nome, email, senha):
        self.setId(id)      # atributo da instância
        self.setNome(nome)
        self.setEmail(email)
        self.setSenha(senha)
        self.__status = False # Em serviço ou não
    def __str__(self):
        return f"{self.getId()} - {self.getNome()} - {self.getEmail()} - {self.getFone()}"

    def getStatus(self):
        return self.__status
    
    def setStatus(self, status):
        if (status == "" or status is None):
            raise ValueError("O valor não pode ser vazio.")-
        self.__status = status

class Clientes(Modelo):    # Persistência - Armazena os objetos em um arquivo/banco de dados
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:     
            with open("entregadores.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Entregador(dic["_Entregador__id"], dic["_Entregador__nome"], dic["_Entregador__email"], dic["_Entregador__senha"])

                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("entregadores.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)