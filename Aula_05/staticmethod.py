import math
class triangulo:                            

    def _init_(self):                       
        self.b = 0
        self.h = 0

    def calc_area(self):                    
        return self.b * self.h / 2
    
class retangulo:                            

    def _init_(self):                       
        self.b = 0
        self.h = 0

    def calc_area(self):                    
        return self.b * self.h / 2
    
class circulo:                            

    def _init_(self):                       
        self.r = 0

    def calc_area(self):                    
        return math.pi * self.r ** 2
    

class UI:
    @staticmethod
    def menu():
        print("Escolha uma opção:")
        print("1 - Triângulo")
        print("2 - Retângulo")
        print("3 - Círculo")
        print("4 - Sair")
        return int(input())
    
    def opTri():
        t = triangulo()
        t.b = float(input('Informe a base do triângulo: '))
        t.h = float(input('Informe a altura do triângulo: '))
        print(f"A área deste triângulo é: {t.calc_area()}")
        

    def opRet():
        r = retangulo()
        r.b = float(input('Informe a base do retângulo: '))
        r.h = float(input('Informe a altura do retângulo: '))
        print(f"A área deste retângulo é: {r.calc_area()}")
        

    def opCir():
        c = circulo()
        c.r = float(input('Informe o raio do círculo: '))
        print(f"A área deste círculo é: {c.calc_area()}")
        

    def main():
        op = 0
        while (op != 4):
            op = UI.menu()
            if op == 1:
                UI.opTri()
            elif op == 2:
                UI.opRet()
            elif op == 3:   
                UI.opCir()
            elif op == 4:   
                print("Saindo...")
            else:
                print("Opção inválida. Tente novamente.")
                UI.main()
            

UI.main()