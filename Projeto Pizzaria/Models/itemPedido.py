import json
from Models.modelo import Modelo

class ItemPedido:
    def __init__(self, id, qtd, preco):
        self.id = id       
        self.qtd = qtd
        self.preco = preco
        self.id_pedido = 0
        self.id_produto = 0
    def __str__(self):
        return f"{self.id} - {self.qtd} - R$ {self.preco:.2f}"

    def setId(self, id):
        if id < 0:
            raise ValueError("O ID não pode ser negativo.")
        self.id = id

    def getId(self):
        return self.id
    
    def setQtd(self, qtd):
        if qtd < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self.qtd = qtd

    def getQtd(self):
        return self.qtd
    
    def setPreco(self, preco):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.preco = preco

    def getPreco(self):
        return self.preco
    
    def setIdPedido(self, id_pedido):
        if id_pedido < 0:
            raise ValueError("O ID da Pedido não pode ser negativo.")
        self.id_pedido = id_pedido

    def getIdPedido(self):
        return self.id_pedido
    
    def setIdProduto(self, id_produto):
        if id_produto < 0:
            raise ValueError("O ID do produto não pode ser negativo.")
        self.id_produto = id_produto

    def getIdProduto(self):
        return self.id_produto

class ItensPedidos(Modelo):    # Persistência - Armazena os objetos em um arquivo/banco de dados
    @classmethod
    def abrir(cls):
        cls.objetos = [] 
        try:   
            with open("itemPedido.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = VendaItem(dic["id"], dic["qtd"], dic["preco"])
                    obj.setIdPedido(dic["id_pedido"])
                    obj.setIdProduto(dic["id_produto"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("itemPedido.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)