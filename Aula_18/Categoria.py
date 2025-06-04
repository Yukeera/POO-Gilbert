import json

class Categoria:
    def __init__(self, id, d):
        self.setId(id)
        self.setD(d)

    def setId(self, id):
        self.__id == id

    def getId(self):
        return self.__id
    
    def setD(self,d):
        self.__d == d

    def getD(self):
        return self.__id
    
    def __str__(self):
        return f"Id = {self.__id}  Descrição = {self.__d}"
    

class Categorias:
    objetos = []

    @classmethod
    def inserir(cls):
        pass
    @classmethod
    def listar(cls):
        return cls.categoriaList
    @classmethod
    def listarId(cls, id):
        for obj in cls.objetos:
            if obj.id == id:
                return obj
            return None
        
    @classmethod
    def atualizar(cls, obj):
        x = cls.listarId(obj.id)
        if (x != None):
            cls.objetos.remove(x)
            cls.objetos.append(obj)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("categorias.json", mode = r) as arquivo:
                s = json.load(arquivo) #PAREI AQUI
            
        except FileNotFoundError:
            pass