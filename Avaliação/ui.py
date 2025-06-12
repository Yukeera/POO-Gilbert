#from cliente import Cliente, Clientes
#from categoria import Categoria, Categorias
#from produto import Produto, Produtos
#from venda import Venda, Vendas
#from vendaitem import VendaItem, VendaItens

from views import View

class UI:  # Classe de Interface com o Usuário (View no padrão)
      # Carrinho de compras atual (compartilhado como atributo de classe)
    id_de_acesso = None

    @staticmethod
    def menuVisitante():
        # Exibe o menu principal com as opções disponíveis ao usuário
        print("|------------------------------------------------|")
        print("| Olá Visitante, bem vindo ao Comércio Virtual   |")
        print("| 97-Entrar no Sistema, 98-Abrir Conta           |")
        print("|------------------------------------------------|")
        print("| 99-FIM                                         |")
        print("|------------------------------------------------|")
        print()
        op = int(input("Selecione uma opção: "))  # Recebe a opção do usuário
        print()
        return op


    @staticmethod
    def menuAdmin():
        # Exibe o menu principal com as opções disponíveis ao usuário
        print("|------------------------------------------------|")
        print("| Valeu Ademir, aí tem moral                     |")
        print("|------------------------------------------------|")
        print("| Cadastro de Clientes                           |")
        print("| 1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir    |")
        print("|------------------------------------------------|")
        print("| Cadastro de Categorias                         |")
        print("| 5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir    |")
        print("|------------------------------------------------|")
        print("| Cadastro de Produtos                           |")
        print("| 9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir |")
        print("|------------------------------------------------|")
        print("| Informações de Vendas                          |")
        print("| 14-Listar Vendas Realizadas                    |")
        print("|------------------------------------------------|")
        print("| 99-FIM , 100-Sair da conta                     |")
        print("|------------------------------------------------|")
        print()
        op = int(input("Selecione uma opção: "))  # Recebe a opção do usuário
        print()
        return op
    

    @staticmethod
    def menuCliente():
        # Exibe o menu principal com as opções disponíveis ao usuário
        print("|------------------------------------------------|")
        print("| Seja bem-vindo novamente, meu semelhante!      |")
        print("|------------------------------------------------|")
        print("| 13-Iniciar um carrinho de compra               |")
        print("| 14-Listar as compras                           |")
        print("| 10-Ver Produtos Disponíveis                    |")
        print("| 15-Visualizar carrinho                         |")
        print("| 16-Inserir produto no carrinho                 |")
        print("| 17-Confirmar a compra                          |")
        print("|------------------------------------------------|")
        print("| 96-Editar Perfil , 95-Ver Meu Perfil           |")
        print("|------------------------------------------------|")
        print("|------------------------------------------------|")
        print("| 99-FIM , 100-Sair da conta                     |")
        print("|------------------------------------------------|")
        print()
        op = int(input("Selecione uma opção: "))  # Recebe a opção do usuário
        print()
        return op

    @classmethod
    def paginaInicial(cls):
        while True:
            tipoUsuario = None
            op = UI.menuVisitante()
            if (op == 97):
                email = input("Digite seu Email: ")
                print()
                senha = input("Digite seu Senha: ")
                print()
                if(View.autenticacao_Usuario(email, senha) != 0):
                    tipoUsuario = "Cliente"
                    if (email == "admin"):
                        tipoUsuario = "Admin"
                    cls.id_de_acesso = View.autenticacao_Usuario(email, senha)
                    break
                else:
                    print('Email Inexistente ou senha inválida, tente novamente, ou crie uma nova conta!')
                    print()
            elif (op == 98):
                UI.cliente_inserir()
                print()
                print("Conta criada com sucesso!")
                print()
            elif (op == 99):
                break
        return tipoUsuario

    @staticmethod
    def main():
        # Loop principal que executa o menu e chama os métodos correspondentes
        View.cadastrar_admin()  # Garante que o usuário admin seja criado no início
        tipoUsuario = UI.paginaInicial()
        
        op = 0
        while op != 99:
            match tipoUsuario:
                case "Cliente":
                    op = UI.menuCliente()
                    if op == 13: UI.venda_inserir()
                    if op == 14: UI.listar_minhas_compras()
                    if op == 10: UI.produto_listar()
                    if op == 15: UI.visualizar_carrinho()
                    if op == 16: UI.inserir_produto_no_carrinho()
                    if op == 17: UI.confirmar_compra()
                    if op == 96: UI.cliente_editar()
                    if op == 95: UI.cliente_visualizar()
                    if op == 100: tipoUsuario = UI.paginaInicial()

                case "Admin":
                    op = UI.menuAdmin()
                    if op == 1: UI.cliente_inserir()
                    if op == 2: UI.cliente_listar()
                    if op == 3: UI.cliente_atualizar()
                    if op == 4: UI.cliente_excluir()

                    if op == 5: UI.categoria_inserir()
                    if op == 6: UI.categoria_listar()
                    if op == 7: UI.categoria_atualizar()
                    if op == 8: UI.categoria_excluir()
                    
                    if op == 9: UI.produto_inserir()
                    if op == 10: UI.produto_listar()
                    if op == 11: UI.produto_atualizar()
                    if op == 12: UI.produto_excluir()
                    if op == 14: UI.venda_listar()
                    if op == 100: tipoUsuario = UI.paginaInicial()

                case None:
                    break



        '''while op != 99:
                
            # Mapeamento das opções do menu para os métodos da UI
            
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()

            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()

            if op == 9: UI.produto_inserir()
            if op == 10: UI.produto_listar()
            if op == 11: UI.produto_atualizar()
            if op == 12: UI.produto_excluir()

            if op == 13: UI.venda_inserir()
            if op == 14: UI.venda_listar()
            if op == 15: UI.visualizar_carrinho()
            if op == 16: UI.inserir_produto_no_carrinho()
            if op == 17: UI.confirmar_compra()
        '''

    # -------------------------
    # CRUD de Clientes
    # -------------------------
    @staticmethod
    def cliente_inserir():
        # Solicita os dados e envia para o View inserir um cliente
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        fone = input("Informe o fone: ")
        View.cliente_inserir(nome, email, senha, fone)

    @staticmethod
    def cliente_listar():
        # Lista todos os clientes cadastrados
        for c in View.cliente_listar():
            print(c)

    @staticmethod
    def cliente_atualizar():
        # Atualiza os dados de um cliente existente
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        senha = input("Informe a nova senha: ")
        fone = input("Informe o novo fone: ")
        View.cliente_atualizar(id, nome, email, senha, fone)

    @staticmethod
    def cliente_excluir():
        # Exclui um cliente pelo ID
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.cliente_excluir(id)

    @classmethod
    def cliente_editar(cls):
        # Permite ao cliente editar seu perfil
        cliente = View.cliente_listar_id(cls.id_de_acesso)
        print("Dados atuais do cliente:")
        print(cliente)
        nome = input("Informe o novo nome (deixe em branco para manter): ") or cliente.getNome()
        email = input("Informe o novo e-mail (deixe em branco para manter): ") or cliente.getEmail()
        senha = input("Informe a nova senha (deixe em branco para manter): ") or cliente.getSenha()
        fone = input("Informe o novo fone (deixe em branco para manter): ") or cliente.getFone()
        View.cliente_atualizar(cls.id_de_acesso, nome, email, senha, fone)

    @classmethod
    def cliente_visualizar(cls):
        # Exibe os dados do cliente atual
        cliente = View.cliente_listar_id(cls.id_de_acesso)
    
        print("Dados do cliente:")
        print(cliente)
    
        print("Compras realizadas:")
        cliente.listarCarrinhosFinalizados()

    # -------------------------
    # CRUD de Categorias
    # -------------------------
    @staticmethod
    def categoria_inserir():
        # Insere uma nova categoria de produto
        descricao = input("Informe a descrição: ")
        View.inserir_categoria(descricao)

    @staticmethod
    def categoria_listar():
        # Lista todas as categorias cadastradas
        for c in View.listar_categorias():
            print(c)

    @staticmethod
    def categoria_atualizar():
        # Atualiza uma categoria existente
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser atualizada: "))
        descricao = input("Informe a nova descrição: ")
        View.atualizar_categoria(id, descricao)

    @staticmethod
    def categoria_excluir():
        # Exclui uma categoria pelo ID
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluída: "))
        View.excluir_categoria(id)

    # -------------------------
    # CRUD de Produtos
    # -------------------------
    @staticmethod
    def produto_inserir():
        # Insere um novo produto associado a uma categoria
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe o estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o id da categoria: "))
        View.inserir_produto(descricao, preco, estoque, id_categoria)

    @staticmethod
    def produto_listar():
        # Lista todos os produtos cadastrados
        for p in View.listar_produtos():
            print(p)

    @staticmethod
    def produto_atualizar():
        # Atualiza as informações de um produto existente
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser atualizado: "))

        print("|------------------------------------------------|")
        print("| Atualização de Produto                         |")
        print("| 1-Reajuste Preço , 2-Informações do produto    |")
        print("|------------------------------------------------|")

        op = int(input(""))
        if (op == 1):
            preco = float(input("Informe o novo preço: "))
            View.atualizar_produto_preço(id, preco)
        elif(op == 2):
            descricao = input("Informe a nova descrição: ")
            preco = float(input("Informe o novo preço: "))
            estoque = int(input("Informe o novo estoque: "))
            UI.categoria_listar()
            id_categoria = int(input("Informe o id da nova categoria: "))
            View.atualizar_produto(id, descricao, preco, estoque, id_categoria)
        
        

    @staticmethod
    def produto_excluir():
        # Exclui um produto pelo ID
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser excluído: "))
        View.excluir_produto(id)

    # -------------------------
    # Operações de Venda / Carrinho
    # -------------------------
    @classmethod
    def venda_inserir(cls):
        # Cria uma nova venda e associa a um carrinho
        View.inserir_venda(cls.id_de_acesso)
        
    @staticmethod
    def venda_listar():
        # Lista todas as vendas confirmadas e seus itens
        View.listar_vendas_com_itens()

    @classmethod
    def visualizar_carrinho(cls):
        # Exibe os produtos no carrinho atual
        if (View.verificar_carrinho(cls.id_de_acesso) == 0):
            return
        carrinho, itens = View.listar_itens_do_carrinho(View.verificar_carrinho(cls.id_de_acesso))
        print("Este é seu carrinho atual:", carrinho)
        for item in itens:
            print(item)

    @classmethod
    def inserir_produto_no_carrinho(cls):
        # Adiciona um produto ao carrinho atual
        if (View.verificar_carrinho(cls.id_de_acesso) == 0):
            return
        UI.produto_listar()
        id_produto = int(input("Informe o id do produto: "))
        qtd = int(input("Informe a qtd: "))
        print (f"id do carrinho : {View.verificar_carrinho(cls.id_de_acesso)}")
        View.inserir_produto_no_carrinho(View.verificar_carrinho(cls.id_de_acesso), id_produto, qtd)

    @classmethod
    def confirmar_compra(cls):
        # Finaliza a compra do carrinho atual
        if View.verificar_carrinho(cls.id_de_acesso) == 0:
            return
        View.confirmar_compra(View.verificar_carrinho(cls.id_de_acesso), cls.id_de_acesso)

    @classmethod
    def listar_minhas_compras(cls):
        View.listar_minhas_compras(cls.id_de_acesso)


# Executa o programa
UI.main()
