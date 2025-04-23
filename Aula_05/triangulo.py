class triangulo:                            

    def _init_(self):
        # B e H foram encapsulados/privados, ou seja, não podem ser acessados diretamente
        # fora da classe. Para acessá-los, é necessário usar os métodos get e set.
        self.__b = 0
        self.__h = 0

    def setAltura(self, h):
        if h > 0:
            self.__h = h
        else:
            raise ValueError("Altura inválida. A altura deve ser maior que zero.")
            # print("Altura inválida. A altura deve ser maior que zero.")

    def setBase(self, b):
        if b > 0:
            self.__b = b
        else:
            raise ValueError("Base inválida. A base deve ser maior que zero.")
            # print("Base inválida. A base deve ser maior que zero.")
    def getAltura(self):
        return self.__h
    
    def getBase(self):
        return self.__b

    def calc_area(self):                    
        return self.__b * self.__h / 2