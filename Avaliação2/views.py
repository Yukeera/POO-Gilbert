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
            raise ValueError
        v = Venda(0, id_cliente)
        Vendas.inserir(v)
        c.setIdCarrinho(v.id)
        Clientes.salvar()
        return 1
    
    @staticmethod
    def clienteCarrinhoCC(id_cliente):   
        # procura um carrinho para o cliente
        for v in Vendas.listar():
            if v.id_cliente == id_cliente and v.carrinho:
                return v.id
        # insere um carrinho novo
        v = Venda(0, id_cliente)
        Vendas.inserir(v)
        v.id_cliente = id_cliente
        return v.id


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
    def listar_carrinhos_finalizados(id_cliente):
        c = Clientes.listar_id(id_cliente)
        return c.getCarrinhosFinalizados()

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
            raise ValueError(f"Estoque insuficiente para o produto {produto.getDescricao()}. Estoque atual: {produto.getEstoque()}")
        elif qtd <= 0:
            raise ValueError("Quantidade inválida. Por favor, insira uma quantidade maior que zero.")

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
            raise ValueError("Você não tem itens no carrinho!")
        for item in VendaItens.listar():
            if item.getIdVenda() == id_carrinho:
                break
        else:
            raise ValueError("Você não tem itens no carrinho!")

        carrinho = Vendas.listar_id(id_carrinho)
        c = Clientes.listar_id(id_de_acesso)
        carrinhoFinalizado = f"Compra :\n{carrinho} \n"

        for item in VendaItens.listar():
            if item.getIdVenda() == id_carrinho:
                try:
                    produto = Produtos.listar_id(item.getIdProduto())
                    produto.setEstoque(produto.getEstoque() - item.getQtd())
                    carrinhoFinalizado += f"{produto.getDescricao()} - Qtd: {item.getQtd()} - R$ {item.getPreco():.2f} \n"
                    Produtos.atualizar(produto)

                    # DUPLICAR venda e itens antes de apagar
                    nova_venda = Venda(0, carrinho.getIdCliente())
                    nova_venda.setData(carrinho.getData())
                    nova_venda.setCarrinho(False)
                    nova_venda.setTotal(carrinho.getTotal())
                    Vendas.inserir(nova_venda)
                    for item in VendaItens.listar():
                        if item.getIdVenda() == carrinho.getId():
                            novo_item = VendaItem(0, item.getQtd(), item.getPreco())
                            novo_item.setIdVenda(nova_venda.getId())
                            novo_item.setIdProduto(item.getIdProduto())
                            VendaItens.inserir(novo_item)

                    VendaItens.excluir(item)
                except:
                    Vendas.excluir(carrinho)

        Vendas.excluir(carrinho)
        c.setIdCarrinho(0)
        c.inserirCarrinhoFinalizado(carrinhoFinalizado)
        Clientes.salvar()

        print("Compra finalizada com sucesso!")

    # Função nova para fazer uma nova compra
    @staticmethod
    def listar_opcoes_recompra(id_cliente):
        opcoes = []
        ids_vendas = []
        for venda in Vendas.listar():
            if venda.getIdCliente() == id_cliente and not venda.getCarrinho():
                desc = f"{venda.getId()} - {venda.getData().strftime('%d/%m/%Y %H:%M')} - R$ {venda.getTotal():.2f}"
                opcoes.append(desc)
                ids_vendas.append(venda.getId())
        return opcoes, ids_vendas

    @staticmethod
    def comprar_novamente(id_cliente, id_venda_antiga):
        carrinho_atual = View.clienteCarrinhoCC(id_cliente)
        if carrinho_atual == 0:
            View.venda_inserir(id_cliente)
            carrinho_atual = View.clienteCarrinhoCC(id_cliente)
        for item in VendaItens.listar():
            if item.getIdVenda() == id_venda_antiga:
                View.carrinho_adicionar_produto(
                    carrinho_atual,
                    item.getIdProduto(),
                    item.getQtd()
                )