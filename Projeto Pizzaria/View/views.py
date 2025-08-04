from Models.cliente import Cliente, Clientes
from Models.categoria import Categoria, Categorias
from Models.produto import Produto, Produtos
from Models.pedido import Pedido, Pedidos
from Models.entregador import Entregador, Entregadores
from Models.itemPedido import ItemPedido, ItensPedidos

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
    def usuario_autenticar(email, senha):
        for c in Clientes.listar():
            if c.getEmail() == email and c.getSenha() == senha:
                return c
        for e in Entregadores.listar():
            if e.getEmail() == email and e.getSenha() == senha:
                return e
        return None

    
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
    def produto_inserir(nome, descricao, preco, estoque, id_categoria):
        if Categorias.listar_id(id_categoria) is None:
            print("Categoria não encontrada. Por favor, crie a categoria primeiro.")
            return
        p = Produto(0, nome, descricao, preco, estoque)
        p.setIdCategoria(id_categoria)
        Produtos.inserir(p)

    @staticmethod
    def produto_listar():
        return Produtos.listar()

    @staticmethod
    def produto_atualizar(id, nome, descricao, preco, estoque, id_categoria):
        if Categorias.listar_id(id_categoria) is None:
            print("Categoria não encontrada. Por favor, crie a categoria primeiro.")
            return
        p = Produto(id, nome, descricao, preco, estoque)
        p.setIdCategoria(id_categoria)
        Produtos.atualizar(p)

    @staticmethod
    def produto_atualizar_preco(id, preco):
        p = Produtos.listar_id(id)
        p.setPreco(preco)
        Produtos.atualizar(p)

    @staticmethod
    def produto_excluir(id):
        p = Produto(id,"Exclusão", "Exclusão", 0, 0)
        Produtos.excluir(p)

        
    # ----------------------------------------
    # Venda / Carrinho - Criação e manipulação
    # ----------------------------------------

    
    @staticmethod
    def clientePedidoCriarChecar(id_cliente):   
        # procura um carrinho para o cliente
        for p in Pedidos.listar():
            if p.id_cliente == id_cliente and p.getStatus() == True:
                return p.id
        # insere um carrinho novo
        p = Pedido(0, id_cliente)
        Pedidos.inserir(p)
        p.setIdCliente(id_cliente)
        return p.id

    
    @staticmethod
    def pedido_itens_listar(id_pedido):
        itens_formatados = []
        pedido = Pedidos.listar_id(id_pedido)
        for item in ItensPedidos.listar():
            if item.getIdPedido() == id_pedido:
                produto = Produtos.listar_id(item.getIdProduto())
                itens_formatados.append(f'{produto.getNome()} - {produto.getDescricao()} - Qtd: {item.getQtd()} - R$ {item.getPreco():.2f} - Subtotal: {item.getQtd() * item.getPreco():.2f}')
        return pedido, itens_formatados

    @staticmethod
    def pedido_adicionar_produto(id_pedido, id_produto, qtd):
        produto = Produtos.listar_id(id_produto)
        preco = produto.getPreco()
        if produto.getEstoque() < qtd:
            raise ValueError(f"Estoque insuficiente para o produto {produto.getDescricao()}. Estoque atual: {produto.getEstoque()}")
        elif qtd <= 0:
            raise ValueError("Quantidade inválida. Por favor, insira uma quantidade maior que zero.")

        vi = ItemPedido(0, qtd, preco)
        vi.setIdPedido(id_pedido)
        vi.setIdProduto(id_produto)
        ItensPedidos.inserir(vi)

        subtotal = qtd * preco
        pedido = Pedidos.listar_id(id_pedido)
        pedido.setTotal(pedido.getTotal() + subtotal)
        Pedidos.atualizar(pedido)

    @staticmethod
    def pedido_confirmar_compra(id_pedido, id_de_acesso):
        if ItensPedidos.listar() is None or len(ItensPedidos.listar()) == 0:
            raise ValueError("Você não tem itens no pedido!")
        for item in ItensPedidos.listar():
            if item.getIdPedido() == id_pedido:
                break
        else:
            raise ValueError("Você não tem itens no pedido!")

        pedido = Pedidos.listar_id(id_pedido)

        for item in ItensPedidos.listar():
            if item.getIdPedido() == id_pedido:
                try:
                    produto = Produtos.listar_id(item.getIdProduto())
                    produto.setEstoque(produto.getEstoque() - item.getQtd())
                    Produtos.atualizar(produto)

                except:
                    Pedidos.excluir(pedido)

        pedido.setStatus(False)  # Marca o pedido como finalizado
        pedido.setStatusEnvio("Em Preparação", 0)  # Define o status de envio
        Pedidos.atualizar(pedido)
        print("Compra finalizada com sucesso!")

    def listar_minhas_compras(id_cliente):
        compras = []
        for pedido in Pedidos.listar():
            if pedido.getIdCliente() == id_cliente and pedido.getStatus() == False:
                compras.append(pedido)
        return compras
    
    def listar_itens_pedido(id_pedido):
        itens = []
        for item in ItensPedidos.listar():
            if item.getIdPedido() == id_pedido:
                produto = Produtos.listar_id(item.getIdProduto())
                itens.append((produto.getNome(), produto.getDescricao(), item.getQtd(), item.getPreco()))
        return itens
    
    def pedido_listar_admin():
        pedidos = []
        for pedido in Pedidos.listar():
            if pedido.getStatus() == False:
                pedidos.append(pedido)
        return pedidos

    # ----------------------------------------
    # Entregador - operações CRUD
    # ----------------------------------------

    @staticmethod
    def entregador_listar():
        return Entregadores.listar()

    @staticmethod
    def entregador_inserir(nome, email, senha):
        e = Entregador(0, nome, email, senha)
        Entregadores.inserir(e)

    @staticmethod
    def entregador_atualizar(id, nome, email, senha):
        e = Entregador(id, nome, email, senha)
        Entregadores.atualizar(e)

    @staticmethod
    def entregador_excluir(id):
        e = Entregador(id, "Exclusão", "Exclusão", "Exclusão")
        Entregadores.excluir(e)

    @staticmethod
    def entregador_listar_id(id):
        return Entregadores.listar_id(id)
    
    @staticmethod
    def pedido_listar_pendentes():
        pedidos = []
        for pedido in Pedidos.listar():
            if pedido.getStatus() == False and pedido.getStatusEnvio()[0] == "Em Preparação":
                pedidos.append(pedido)
        return pedidos
    
    @staticmethod
    def pedido_atualizar_status_envio(id_pedido, status_envio, id_entregador):
        pedido = Pedidos.listar_id(id_pedido)
        if pedido is None:
            raise ValueError("Pedido não encontrado.")
        pedido.setStatusEnvio(status_envio, id_entregador)
        Pedidos.atualizar(pedido)

        e = Entregadores.listar_id(id_entregador)
        if(status_envio == "Entregue"):
            e.setStatus(False)
            Entregadores.atualizar(e)
            return
        e.setStatus(True)
        Entregadores.atualizar(e)

    @staticmethod
    def listar_minhas_entregas(id_entregador):
        entregas = []
        for pedido in Pedidos.listar():
            if pedido.getStatusEnvio()[1] == id_entregador and pedido.getStatus() == False:
                entregas.append(pedido)
        return entregas