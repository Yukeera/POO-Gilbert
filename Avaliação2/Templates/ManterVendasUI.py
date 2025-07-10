import streamlit as st
import pandas as pd
from views import View
import time
from Models.venda import Vendas


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
                st.rerun()
            except ValueError as erro:
                st.warning(erro)
                time.sleep(2)
                st.rerun()

    
    def iniciarCarrinho():
        try:
            if(View.venda_inserir(st.session_state["cliente_id"])):
                st.success("Carrinho Iniciado!")
                time.sleep(2)
                st.rerun()
        except:
            st.warning("Você já tem um carrinho aberto. Por favor, finalize a compra antes de criar um novo!")
            time.sleep(2)
            st.rerun()

    
    def verMeuCarrinho():
        if(View.carrinho_verificar(st.session_state["cliente_id"]) == 0):
            st.warning("Você precisa iniciar um carrinho primeiro!")
            time.sleep(2)
            st.rerun()
        else:
            st.header("Meu Carrinho")
            carrinho, itens = View.venda_itens_listar(View.carrinho_verificar(st.session_state["cliente_id"]))
            st.write(carrinho)
            for item in itens:
                st.write(item)
            time.sleep(2)
            st.rerun()

    def confirmarCompra():
        if(View.carrinho_verificar(st.session_state["cliente_id"]) == 0):
            st.warning("Você precisa iniciar um carrinho primeiro!")
            time.sleep(2)
            st.rerun()
        else:
            try:
                View.carrinho_confirmar_compra(View.carrinho_verificar(st.session_state["cliente_id"]),st.session_state["cliente_id"])
                st.success("Compra Finalizada!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.warning(erro)
                time.sleep(2)
                st.rerun()

    # Tela para recomprar
    def tela_comprar_novamente(cliente):
        st.title("Comprar Novamente")
        compras = View.listar_carrinhos_finalizados(cliente.getId())
        if not compras:
            st.warning("Você ainda não tem compras finalizadas.")
            return
        opcoes = []
        ids_vendas = []
        for venda in Vendas.listar():
            if venda.getIdCliente() == cliente.getId() and venda.getCarrinho() == False:
                desc = f"{venda.getId()} - {venda.getData().strftime('%d/%m/%Y %H:%M')} - R$ {venda.getTotal():.2f}"
                opcoes.append(desc)
                ids_vendas.append(venda.getId())
        if not opcoes:
            st.info("Nenhuma compra disponível para repetir.")
            return
        escolha = st.selectbox("Selecione uma compra:", opcoes)
        if 'comprar_novamente_clicado' not in st.session_state:
            st.session_state['comprar_novamente_clicado'] = False
        if st.button("Adicionar itens ao carrinho") and not st.session_state['comprar_novamente_clicado']:
            st.session_state['comprar_novamente_clicado'] = True
            index = opcoes.index(escolha)
            id_venda_antiga = ids_vendas[index]
            try:
                View.comprar_novamente(cliente.getId(), id_venda_antiga)
                st.success("Itens adicionados ao carrinho com sucesso!")
                time.sleep(2)
                st.session_state['comprar_novamente_clicado'] = False  # resetar antes do rerun
                st.rerun()
            except ValueError as e:
                st.warning(f"Erro ao adicionar itens: {e}")
                st.session_state['comprar_novamente_clicado'] = False
            except Exception as e:
                st.error(f"Erro inesperado: {e}")
                st.session_state['comprar_novamente_clicado'] = False