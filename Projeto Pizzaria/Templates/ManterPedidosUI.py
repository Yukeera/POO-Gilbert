import streamlit as st
import pandas as pd
from View.views import View
import time
from Models.pedido import Pedidos


class ManterPedidosUI:
    def verificarCompras_Admin():
        st.header("Compras dos Clientes")
        tab1 = st.tabs(["Listar Compras"])[0]
        with tab1:
            ManterPedidosUI.listarAdmin()

    def listarAdmin():
        pedidos = View.pedido_listar_admin()
        if len(pedidos) == 0:
            st.write("Nenhuma compra foi realizada ainda.")
        else:
            list_dic = [{"ID": obj.getId(), "Data": obj.getData(), "Total": obj.getTotal(), "ID Cliente": obj.getIdCliente(), "Status Envio": obj.getStatusEnvio()[0]} for obj in pedidos] 
            df = pd.DataFrame(list_dic)
            st.dataframe(df)


    def inserirProdutoNoPedido():
        if(View.clientePedidoCriarChecar(st.session_state["usuario_id"]) == 0):
             st.warning("Você precisa criar um pedido primeiro!")
             return
        st.header("Adicionar Produto no Pedido")
        produtos = View.produto_listar()
        if (len(produtos) == 0):
            st.warning("Não há produtos cadastrados no sistema :(")
            return
        produtoEscolhido = st.selectbox("Selecione o Produto que deseja", produtos)
        quant = st.number_input("Informe a Quantidade de Produtos que deseja", min_value= 1)
        if (st.button("Adicionar")):
            try:
                View.pedido_adicionar_produto(View.clientePedidoCriarChecar(st.session_state["usuario_id"]), produtoEscolhido.getId(), quant)
                st.success("Item Adicionado!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.warning(erro)
                time.sleep(2)
                st.rerun()

    
    def iniciarCarrinho():
        try:
            if(View.pedido_inserir(st.session_state["cliente_id"])):
                st.success("Carrinho Iniciado!")
                time.sleep(2)
                st.rerun()
        except:
            st.warning("Você já tem um carrinho aberto. Por favor, finalize a compra antes de criar um novo!")
            time.sleep(2)
            st.rerun()

    
    def verMeuPedido():
        st.header("Meu Pedido")
        pedido, itens = View.pedido_itens_listar(View.clientePedidoCriarChecar(st.session_state["usuario_id"]))
        st.write(pedido)
        for item in itens:
            st.write(item)

    def confirmarCompra():
        if(View.clientePedidoCriarChecar(st.session_state["usuario_id"]) == 0):
            st.warning("Você precisa iniciar um carrinho primeiro!")
            time.sleep(2)
            st.rerun()
        else:
            try:
                View.pedido_confirmar_compra(View.clientePedidoCriarChecar(st.session_state["usuario_id"]),st.session_state["usuario_id"])
                st.success("Compra Finalizada!")
            except ValueError as erro:
                st.warning(erro)
                time.sleep(2)
                st.rerun()

    def despachar_pedido():
        pedidos = View.pedido_listar_pendentes()
        if len(pedidos) == 0:
            st.write("Nenhum pedido pendente")
        else:
            op = st.selectbox("Atualizar Status do Pedido", pedidos)
            status = st.selectbox("Novo Status", ["Em Rota"])
            entregador = st.selectbox("Selecione o Entregador", View.entregador_listar())
            if st.button("Atualizar"):
                try:
                    View.pedido_atualizar_status_envio(op.getId(), status, entregador.getId())
                
                    st.success("Status do pedido atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                    time.sleep(2)
                    st.rerun()
