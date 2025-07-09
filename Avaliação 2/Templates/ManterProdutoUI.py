import streamlit as st
import pandas as pd
from views import View
import time

class ManterProdutoUI:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()
    def listar():
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            list_dic = []
            for obj in produtos:
                dic = obj.__dict__
                list_dic.append(dic)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        descricao = st.text_input("Informe a descrição do produto:")
        preco = st.number_input("Informe o preço do produto:")
        categorias = View.categoria_listar()
        if len(categorias) == 0:
            st.warning("Cadastre pelo menos uma categoria antes de inserir produtos.")
            return
        cat = st.selectbox("Selecione a categoria:", categorias)
        if st.button("Cadastrar"):
            try:
                View.produto_inserir(descricao, preco, cat.get_id())
                st.success("Produto inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(f"Erro: {erro}")
                time.sleep(2)
                st.rerun()
    def atualizar():
        produtos = View.produto_listar()
        categorias = View.categoria_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
            return
        if len(categorias) == 0:
            st.warning("Cadastre uma categoria antes de atualizar produtos.")
            return
        op = st.selectbox("Atualização de produto", produtos)
        nova_desc = st.text_input("Informe a nova descrição:", op.get_descricao())
        novo_preco = st.number_input("Informe o novo preço:", op.get_preco())
        nova_cat = st.selectbox("Selecione a nova categoria:", categorias)
        if st.button("Atualizar"):
            try:
                View.produto_atualizar(op.get_id(), nova_desc, novo_preco, nova_cat.get_id())
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(f"Erro: {erro}")
                time.sleep(2)
                st.rerun()
    def excluir():
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de produto", produtos)
            if st.button("Excluir"):
                try:
                    View.produto_excluir(op.get_id())
                    st.success("Produto excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(f"Erro: {erro}")
                    time.sleep(2)
                    st.rerun()