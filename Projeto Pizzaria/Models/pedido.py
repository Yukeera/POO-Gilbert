import json
from datetime import datetime
import pytz
from Models.modelo import Modelo
import streamlit as st

class Pedido:
    def __init__(self, id, id_cliente):
        self.setId(id)
        self.setData(datetime.now(pytz.timezone('America/Sao_Paulo')))
        self.setStatus(True)
        self.setTotal(0)
        self.setIdCliente(id_cliente)
        self.statusEnvio = (None, 0)  # Indica se o pedido foi enviado ou não

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

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        if not isinstance(status, bool):
            raise ValueError("O status deve ser um valor booleano.")
        self.status = status

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

    def getStatusEnvio(self):
        return self.statusEnvio
    
    def setStatusEnvio(self, status_envio, id_entregador):
        self.statusEnvio = (status_envio, id_entregador)

    def to_json(self):
        dic = {}
        dic["id"] = self.getId()
        dic["data"] = self.getData().strftime("%d/%m/%Y %H:%M")
        dic["status"] = self.getStatus()
        dic["total"] = self.getTotal()
        dic["id_cliente"] = self.getIdCliente()
        dic["status_envio"] = self.getStatusEnvio()
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
                    obj.setStatus(dic["status"])
                    obj.setTotal(dic["total"])
                    obj.setIdCliente(dic["id_cliente"])
                    obj.setStatusEnvio(dic["status_envio"][0], dic["status_envio"][1])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("pedidos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Pedido.to_json)
