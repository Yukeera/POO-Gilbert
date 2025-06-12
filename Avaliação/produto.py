import json

class Produto:
    def __init__(self, id, descricao, preco, estoque):
        self.setId(id)      # atributo da instância
        self.setDescricao(descricao)
        self.setPreco(preco)
        self.setEstoque(estoque)      
        self.__id_categoria = 0
    def __str__(self):
        return f"{self.getId()} - {self.getDescricao()} - R$ {self.getPreco():.2f} - estoque: {self.getEstoque()}"
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        if id < 0:
            raise ValueError("O ID não pode ser negativo.")
        self.__id = id

    def getDescricao(self):
        return self.__descricao

    def setDescricao(self, descricao):
        if descricao == "" or descricao is None:
            raise ValueError("A descrição não pode ser vazia.")
        self.__descricao = descricao

    def getPreco(self):
        return self.__preco
    
    def setPreco(self, preco):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.__preco = preco

    def getEstoque(self):
        return self.__estoque

    def setEstoque(self, estoque):
        if estoque < 0:
            raise ValueError("O estoque não pode ser negativo.")
        self.__estoque = estoque

    def setIdCategoria(self, id_categoria):
        if id_categoria < 0:
            raise ValueError("O ID da categoria não pode ser negativo.")
        self.__id_categoria = id_categoria

    def getIdCategoria(self):
        return self.__id_categoria

class Produtos:    # Persistência - Armazena os objetos em um arquivo/banco de dados
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
            with open("produtos.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Produto(dic["_Produto__id"], dic["_Produto__descricao"], dic["_Produto__preco"], dic["_Produto__estoque"])
                    obj.setIdCategoria(dic["_Produto__id_categoria"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)