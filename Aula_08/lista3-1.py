import math

class Retangulo:
    def __init__(self, b, h):
        if (b <= 0 or h <= 0):
            raise ValueError("Base e altura devem ser maiores que zero.")
        self.__base = b
        self.__altura = h

    def setBase(self, b):
        if (b > 0):
            self.__base = b
        else: 
            raise ValueError("A Base deve ser maior que zero ")

    def setAltura(self, h):
        if (h > 0):
            self.__altura = h
        else:
            raise ValueError("A altura deve ser maior que zero")
        
    def getBase(self):
        return self.__base
    
    def getAltura(self):
        return self.__altura
    
    def calcArea(self):
        return self.__base * self.__altura
    
    def calcDiagonal(self):
        return math.sqrt((self.__base*self.__base) + (self.__altura * self.__altura))
    
    def __str__(self):
        return f"Eu sou um retangulo e tenho {self.__altura} de altura e {self.__base} de base!"
    
