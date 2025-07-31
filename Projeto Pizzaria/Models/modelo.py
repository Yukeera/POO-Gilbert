from abc import ABC, abstractmethod
class Modelo(ABC):
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
    @abstractmethod
    def abrir(cls):
        pass
    @classmethod
    @abstractmethod
    def salvar(cls):
        pass
