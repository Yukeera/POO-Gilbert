from datetime import datetime, timedelta

class treino:
    def __init__(self, id, idAtleta, data, dist, tempo):
        #self.__id = id
        #self.__idAtleta = idAtleta
        #self.__data = data
        #self.__dist = dist
        #self.__tempo = tempo
        treino.id = id
        treino.idAtleta = idAtleta
        treino.data = data
        treino.dist = dist
        treino.tempo = tempo

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if (id <= 0):
            raise ValueError("O Id deve ser maior que zero!")
        self.__id = id

    @property
    def idAtleta(self):
        return self.__idAtleta
    
    @idAtleta.setter
    def idAtleta(self, idAtleta):
        if (idAtleta <= 0):
            raise ValueError("O Id do atleta deve ser maior que zero!")
        
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

        
    @property
    def dist(self):
        return self.__dist
    
    @dist.setter
    def dist(self, dist):
        if (dist < 0):
            raise ValueError("A distância deve ser positivo!")
        
    @property
    def tempo(self):
        return self.__tempo
    
    @tempo.setter
    def tempo(self, tempo):
        if(tempo <= 0):
            raise ValueError("O tempo deve ser maior que zero!")
        self.__tempo = tempo

    def pace(self):
        return (self.__tempo.seconds / 60) / (self.__dist / 1000)

    def __str__(self):
        s =  f"Data = {self.__data.strftime("%d/%m/%Y %H:%M")}"
        s += f" Distância = {self.__dist} metros"
        s += f"Tempo = {self.__tempo}"
        return s
    
    
x = treino(1, 1, datetime(2025 , 5 , 12 , 6 , 45), 5000, timedelta(minutes = 30))
y = treino(1, 1, datetime(2025 , 5 , 14 , 6 , 30), 5000, timedelta(minutes = 30, seconds=45))

print(x)
print("Pace = ", x.pace(), "min/km")
print (y)
print("Pace =", y.pace(), "min/km")