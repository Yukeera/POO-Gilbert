from Models.cliente import Cliente, Clientes
from Models.categoria import Categoria, Categorias
from Models.produto import Produto, Produtos
from Models.venda import Venda, Vendas
from Models.vendaitem import VendaItem, VendaItens

class View:

    # ----------------------------------------
    # Cliente - Operações CRUD
    # ----------------------------------------

    @staticmethod
    def cadastrar_admin():
        for cliente in Clientes.listar():
            if cliente.getEmail() == "admin":
                return
        View.cliente_inserir("admin", "admin", "admin", "1234")

    @staticmethod
    def cliente_inserir(nome, email, senha, fone):
        c = Cliente(0, nome, email, senha, fone)
        Clientes.inserir(c)

    @staticmethod
    def cliente_listar():
        return Clientes.listar()

    @staticmethod
    def cliente_listar_id(id):
        return Clientes.listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, senha, fone):
        c = Cliente(id, nome, email, senha, fone)
        Clientes.atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, "Exclusão", "Exclusão", "Exclusão", "Exclusão")
        Clientes.excluir(c)

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Clientes.listar():
            if c.getEmail() == email and c.getSenha() == senha:
                return c
        return None

    @staticmethod
    def cliente_listar_compras(id_de_acesso):
        c = Clientes.listar_id(id_de_acesso)
        c.listarCarrinhosFinalizados()

    # ----------------------------------------
    # Categoria - Operações CRUD
    # ----------------------------------------

    @staticmethod
    def categoria_inserir(descricao):
        c = Categoria(0, descricao)
        Categorias.inserir(c)

    @staticmethod
    def categoria_listar():
        return Categorias.listar()

    @staticmethod
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        Categorias.atualizar(c)

    @staticmethod
    def categoria_excluir(id):
        c = Categoria(id, "Exclusão")
        Categorias.excluir(c)

    # ----------------------------------------
    # Produto - Operações CRUD
    # ----------------------------------------

    @staticmethod
    def produto_inserir(descricao, preco, estoque, id_categoria):
        if Categorias.listar_id(id_categoria) is None:
            print("Categoria não encontrada. Por favor, crie a categoria primeiro.")
            return
        p = Produto(0, descricao, preco, estoque)
        p.setIdCategoria(id_categoria)
        Produtos.inserir(p)

    @staticmethod
    def produto_listar():
        return Produtos.listar()

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        if Categorias.listar_id(id_categoria) is None:
            print("Categoria não encontrada. Por favor, crie a categoria primeiro.")
            return
        p = Produto(id, descricao, preco, estoque)
        p.setIdCategoria(id_categoria)
        Produtos.atualizar(p)

    @staticmethod
    def produto_atualizar_preco(id, preco):
        p = Produtos.listar_id(id)
        p.setPreco(preco)
        Produtos.atualizar(p)

    @staticmethod
    def produto_excluir(id):
        p = Produto(id, "Exclusão", 0, 0)
        Produtos.excluir(p)

    # ----------------------------------------
    # Venda / Carrinho - Criação e manipulação
    # ----------------------------------------

    @staticmethod
    def venda_inserir(id_cliente):
        c = Clientes.listar_id(id_cliente)
        if c.getIdCarrinho() != 0:
            print(f"Você já tem um carrinho aberto com o id {c.getIdCarrinho()}. Por favor, finalize a compra antes de criar um novo.")
            return
        v = Venda(0, id_cliente)
        Vendas.inserir(v)
        c = Clientes.listar_id(id_cliente)
        if c.getIdCarrinho() != 0:
            print(f"Você já tem um carrinho aberto com o id {c.getIdCarrinho()}. Por favor, finalize a compra antes de criar um novo.")
            return
        c.setIdCarrinho(v.id)
        Clientes.salvar()

    @staticmethod
    def carrinho_verificar(id_cliente):
        c = Clientes.listar_id(id_cliente)
        if c.getIdCarrinho() == 0:
            print("Você precisa criar um carrinho primeiro!")
            return 0
        else:
            return c.getIdCarrinho()

    @staticmethod
    def venda_listar_terminal():
        for c in Clientes.listar():
            if len(c.getCarrinhosFinalizados()) > 0:
                print(f"Cliente: \n {c} \n")
                c.listarCarrinhosFinalizados()

    @staticmethod
    def venda_listar_admin():
        vendas_formatadas = []
        for c in Clientes.listar():
            for carrinho in c.getCarrinhosFinalizados():
                vendas_formatadas.append({
                    "cliente_id": c.getId(),
                    "cliente_nome": c.getNome(),
                    "descricao": carrinho
                })
        return vendas_formatadas

    @staticmethod
    def venda_itens_listar(id_carrinho):
        itens_formatados = []
        carrinho = Vendas.listar_id(id_carrinho)
        for item in VendaItens.listar():
            if item.getIdVenda() == id_carrinho:
                produto = Produtos.listar_id(item.getIdProduto())
                itens_formatados.append(f"  {produto.getDescricao()} - Qtd: {item.getQtd()} - R$ {item.getPreco():.2f}")
        return carrinho, itens_formatados

    @staticmethod
    def carrinho_adicionar_produto(id_carrinho, id_produto, qtd):
        produto = Produtos.listar_id(id_produto)
        preco = produto.getPreco()
        if produto.getEstoque() < qtd:
            print(f"Estoque insuficiente para o produto {produto.getDescricao()}. Estoque atual: {produto.getEstoque()}")
            return
        elif qtd <= 0:
            print("Quantidade inválida. Por favor, insira uma quantidade maior que zero.")
            return

        vi = VendaItem(0, qtd, preco)
        vi.setIdVenda(id_carrinho)
        vi.setIdProduto(id_produto)
        VendaItens.inserir(vi)

        subtotal = qtd * preco
        carrinho = Vendas.listar_id(id_carrinho)
        carrinho.setTotal(carrinho.getTotal() + subtotal)
        Vendas.atualizar(carrinho)

    @staticmethod
    def carrinho_confirmar_compra(id_carrinho, id_de_acesso):
        if VendaItens.listar() is None or len(VendaItens.listar()) == 0:
            print("Você não tem itens no carrinho!")
            return
        for item in VendaItens.listar():
            if item.getIdVenda() == id_carrinho:
                break
        else:
            print("Você não tem itens no carrinho!")
            return

        carrinho = Vendas.listar_id(id_carrinho)
        c = Clientes.listar_id(id_de_acesso)
        carrinhoFinalizado = f"Compra :\n{carrinho} \n"
        Vendas.excluir(carrinho)

        for item in VendaItens.listar():
            if item.getIdVenda() == id_carrinho:
                produto = Produtos.listar_id(item.getIdProduto())
                carrinhoFinalizado += f"{produto.getDescricao()} - Qtd: {item.getQtd()} - R$ {item.getPreco():.2f} \n"

        c.setIdCarrinho(0)
        c.inserirCarrinhoFinalizado(carrinhoFinalizado)
        Clientes.salvar()

        for item in VendaItens.listar():
            if item.getIdVenda() == id_carrinho:
                produto = Produtos.listar_id(item.getIdProduto())
                produto.setEstoque(produto.getEstoque() - item.getQtd())
                Produtos.atualizar(produto)
                VendaItens.excluir(item)

        print("Compra finalizada com sucesso!")
