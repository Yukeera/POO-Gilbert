import contabancaria

class UI:
    @staticmethod
    def menu():
        print("Escolha uma opção:")
        print("1 - Abrir conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Ver saldo")
        return int(input())
    
    @staticmethod
    def abrirConta():
        x = contabancaria.ContaBancaria()
        print("Digite o nome do titular:")
        titular = input()
        print("Digite o número da conta:")
        numero = input()
    
    def depositar(x):
        print("Digite o valor a ser depositado:")
        valor = float(input())
        x.depositar(valor)
        print(f"Depósito de {valor} realizado com sucesso.")

    def sacar(x):
        print("Digite o valor a ser sacado:")
        valor = float(input())
        try:
            x.sacar(valor)
            print(f"Saque de {valor} realizado com sucesso.")
        except ValueError as e:
            print(e)

    def main():
        op = 0
        while (op != 4):
            op = UI.menu()
            if op == 1:
                x = UI.abrirConta()
            elif op == 2:
                UI.depositar(x)
            elif op == 3:   
                UI.sacar(x)
            elif op == 4:   
                
            else:
                print("Opção inválida. Tente novamente.")
                UI.main()
            

UI.main()