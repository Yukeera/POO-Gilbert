import json

class VendaItem:
    def __init__(self, id, qtd, preco):
        self.id = id       
        self.qtd = qtd
        self.preco = preco
        self.id_venda = 0
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
    
    def setIdVenda(self, id_venda):
        if id_venda < 0:
            raise ValueError("O ID da venda não pode ser negativo.")
        self.id_venda = id_venda

    def getIdVenda(self):
        return self.id_venda
    
    def setIdProduto(self, id_produto):
        if id_produto < 0:
            raise ValueError("O ID do produto não pode ser negativo.")
        self.id_produto = id_produto

    def getIdProduto(self):
        return self.id_produto

class VendaItens:    # Persistência - Armazena os objetos em um arquivo/banco de dados
    objetos = []     # atributo de classe / estático - Não tem instância
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
            with open("vendaitens.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = VendaItem(dic["id"], dic["qtd"], dic["preco"])
                    obj.setIdVenda(dic["id_venda"])
                    obj.setIdProduto(dic["id_produto"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("vendaitens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)