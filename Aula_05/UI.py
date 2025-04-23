import circulo
import retangulo
import triangulo

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
        t = triangulo.triangulo()
        t.setBase(float(input('Informe a base do triângulo: ')))
        t.setAltura(float(input('Informe a altura do triângulo: ')))
        print(f"A área deste triângulo onde a base é {t.getBase()} e a altura é {t.getAltura()} é: {t.calc_area()}")
        

    def opRet():
        r = retangulo.retangulo()
        r.b = float(input('Informe a base do retângulo: '))
        r.h = float(input('Informe a altura do retângulo: '))
        print(f"A área deste retângulo é: {r.calc_area()}")
        

    def opCir():
        c = circulo.circulo()
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