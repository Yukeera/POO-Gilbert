class Frete:
    def __init__(self,  distancia, peso):
        if (distancia > 0 and peso > 0):
            self.__distancia = distancia
            self.__peso = peso
        else:
            raise ValueError("Entrada de Distancia e Peso devem ser maiores que 0!")
    
    def setDistancia(self, distancia):
        self.__distancia = distancia

    def setPeso(self, peso):
        self.__peso

    def getDistancia(self):
        return self.__distancia
    
    def getPeso(self):
        return self.__peso
    
    def calcFrete(self):
        return 0.01 * self.__distancia
    
    def __str__(self):
        return f"Sou o frete, e tenho {self.__distancia} de distancia e {self.__peso} de peso!"
    
    