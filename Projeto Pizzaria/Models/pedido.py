import json
from datetime import datetime
import pytz
from Models.modelo import Modelo

class Pedido:
    def __init__(self, id, id_cliente):
        self.setId(id)
        self.setData(datetime.now(pytz.timezone('America/Sao_Paulo')))
        self.setPedido(True)
        self.setTotal(0)
        self.setIdCliente(id_cliente)

    def __str__(self):
        return f"{self.getId()} - {self.getData().strftime('%d/%m/%Y %H:%M')} - R$ {self.getTotal():.2f}"

    def getId(self):
        return self.id
    
    def setId(self, id):
        if id < 0:
            raise ValueError("O ID não pode ser negativo.")
        self.id = id

    def getData(self):
        return self.data
    
    def setData(self, data):
        if not isinstance(data, datetime):
            raise ValueError("A data deve ser um objeto datetime.")
        self.data = data

    def getPedido(self):
        return self.pedido
    
    def setPedido(self, pedido):
        if not isinstance(pedido, bool):
            raise ValueError("O carrinho deve ser um valor booleano.")
        self.pedido = pedido

    def getTotal(self):
        return self.total
    
    def setTotal(self, total):
        if total < 0:
            raise ValueError("O total não pode ser negativo.")
        self.total = total

    def getIdCliente(self):
        return self.id_cliente
    
    def setIdCliente(self, id_cliente):
        if id_cliente < 0:
            raise ValueError("O ID do cliente não pode ser negativo.")
        self.id_cliente = id_cliente

    

    def to_json(self):
        dic = {}
        dic["id"] = self.getId()
        dic["data"] = self.getData().strftime("%d/%m/%Y %H:%M")
        dic["pedido"] = self.getPedido()
        dic["total"] = self.getTotal()
        dic["id_cliente"] = self.getIdCliente()
        return dic
    
class Pedidos(Modelo):      # Persistência - Armazena os objetos em um arquivo/banco de dados
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:     
            with open("pedidos.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Pedido(dic["id"], dic["id_cliente"])
                    obj.setData(datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
                    obj.setPedido(dic["carrinho"])
                    obj.setTotal(dic["total"])
                    obj.setIdCliente(dic["id_cliente"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("pedidos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Pedido.to_json)
