import json
from datetime import datetime

class Venda:
    def __init__(self, id, id_cliente):
        self.setId(id)
        self.setData(datetime.now())
        self.setCarrinho(True)
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

    def getCarrinho(self):
        return self.carrinho
    
    def setCarrinho(self, carrinho):
        if not isinstance(carrinho, bool):
            raise ValueError("O carrinho deve ser um valor booleano.")
        self.carrinho = carrinho

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
        dic["carrinho"] = self.getCarrinho()
        dic["total"] = self.getTotal()
        dic["id_cliente"] = self.getIdCliente()
        return dic
    
class Vendas:      # Persistência - Armazena os objetos em um arquivo/banco de dados
    objetos = []   # atributo de classe / estático - Não tem instância

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for x in cls.objetos:
            if x.getId() > m: m = x.getId()
        obj.setId(m + 1)    
        cls.objetos.append(obj)
        cls.salvar() 
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.getId() == id: return obj
        return None               
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.getId())
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.getId())
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:     
            with open("vendas.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Venda(dic["id"], dic["id_cliente"])
                    obj.setData(datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
                    obj.setCarrinho(dic["carrinho"])
                    obj.setTotal(dic["total"])
                    obj.setIdCliente(dic["id_cliente"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Venda.to_json)
