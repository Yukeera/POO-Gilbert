import streamlit as st
import pandas as pd
from views import View
import time


class ManterVendasUI:
    def verificarCompras_Admin():
        st.header("Compras dos Clientes")
        tab1 = st.tabs(["Listar Compras"])[0]
        with tab1:
            ManterVendasUI.listarAdmin()

    def listarAdmin():
        vendas = View.venda_listar_admin()
        if len(vendas) == 0:
            st.write("Nenhuma compra foi realizada ainda.")
        else:
            df = pd.DataFrame(vendas)
            st.dataframe(df)


    def inserirProdutoNoCarrinho():
        if(View.carrinho_verificar(st.session_state["cliente_id"]) == 0):
             st.warning("Você precisa criar um carrinho primeiro!")
             return
        st.header("Adicionar Produto no Carrinho")
        produtos = View.produto_listar()
        if (len(produtos) == 0):
            st.warning("Não há produtos cadastrados no sistema :(")
            return
        produtoEscolhido = st.selectbox("Selecione o Produto que deseja", produtos)
        quant = st.number_input("Informe a Quantidade de Produtos que deseja", min_value= 1)
        if (st.button("Adicionar")):
            try:
                View.carrinho_adicionar_produto(View.carrinho_verificar(st.session_state["cliente_id"]), produtoEscolhido.getId(), quant)
                st.success("Item Adicionado!")
                time.sleep(2)
                st.rerun
            except ValueError as erro:
                st.warning(erro)
                time.sleep(2)
                st.rerun

    
    def iniciarCarrinho():
        try:
            if(View.venda_inserir(st.session_state["cliente_id"])):
                st.success("Carrinho Iniciado!")
                time.sleep(2)
                st.rerun()
        except:
            st.warning("Você já tem um carrinho aberto. Por favor, finalize a compra antes de criar um novo!")
            time.sleep(2)
            st.rerun

    
    def verMeuCarrinho():
        if(View.carrinho_verificar(st.session_state["cliente_id"]) == 0):
            st.warning("Você precisa iniciar um carrinho primeiro!")
            time.sleep(2)
            st.rerun
        else:
            st.header("Meu Carrinhuo")
            carrinho, itens = View.venda_itens_listar(View.carrinho_verificar(st.session_state["cliente_id"]))
            st.write(carrinho)
            for item in itens:
                st.write(item)
            time.sleep(2)
            st.rerun

    def confirmarCompra():
        if(View.carrinho_verificar(st.session_state["cliente_id"]) == 0):
            st.warning("Você precisa iniciar um carrinho primeiro!")
            time.sleep(2)
            st.rerun
        else:
            try:
                View.carrinho_confirmar_compra(View.carrinho_verificar(st.session_state["cliente_id"]),st.session_state["cliente_id"])
                st.success("Compra Finalizada!")
                time.sleep(2)
                st.rerun
            except ValueError as erro:
                st.warning(erro)
                time.sleep(2)
                st.rerun