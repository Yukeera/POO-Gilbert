import json
from Models.modelo import Modelo

class Cliente:   # Domínio - Entidades - Várias instâncias
    def __init__(self, id, nome, email, senha, fone):
        self.setId(id)      # atributo da instância
        self.setNome(nome)
        self.setEmail(email)
        self.setSenha(senha)
        self.setFone(fone)
        self.__id_carrinho = 0
        self.__carrinhosFinalizados = []
    def __str__(self):
        return f"{self.getId()} - {self.getNome()} - {self.getEmail()} - {self.getFone()}"

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

    def getFone(self):
        return self.__fone
    
    def setFone(self, fone):
        if (fone == "" or fone is None):
            raise ValueError("O telefone não pode ser vazio.")
        self.__fone = fone

    def setIdCarrinho(self, id_carrinho):
        if (id_carrinho is None or id_carrinho < 0):
            raise ValueError("O ID do carrinho não pode ser negativo ou nulo.")
        self.__id_carrinho = id_carrinho

    def getIdCarrinho(self):
        return self.__id_carrinho

    def getCarrinhosFinalizados(self):
        return self.__carrinhosFinalizados
    
    def setCarrinhosFinalizados(self, carrinhosFinalizados):
        if (carrinhosFinalizados is None):
            raise ValueError("A lista de carrinhos finalizados não pode ser nula.")
        self.__carrinhosFinalizados = carrinhosFinalizados

    def inserirCarrinhoFinalizado(self, carrinhoFinalizado):
        if (carrinhoFinalizado is None):
            raise ValueError("O carrinho finalizado não pode ser nulo.")
        self.__carrinhosFinalizados.append(carrinhoFinalizado)

    def listarCarrinhosFinalizados(self):
        if (len(self.__carrinhosFinalizados) == 0):
            print("Você não realizou compra alguma!")
            return 0
        for carrinho in self.__carrinhosFinalizados:
            print(carrinho)
        return 1

class Clientes(Modelo):    # Persistência - Armazena os objetos em um arquivo/banco de dados
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:     
            with open("clientes.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Cliente(dic["_Cliente__id"], dic["_Cliente__nome"], dic["_Cliente__email"], dic["_Cliente__senha"], dic["_Cliente__fone"])
                    obj.setIdCarrinho(dic["_Cliente__id_carrinho"])
                    obj.setCarrinhosFinalizados(dic["_Cliente__carrinhosFinalizados"])

                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)