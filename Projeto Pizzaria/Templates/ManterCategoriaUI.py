import streamlit as st
import pandas as pd
from View.views import View
import time

class ManterCategoriaUI:
    def main():
        st.header("Cadastro de Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.inserir()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()

    def listar():
        categorias = View.categoria_listar()
        if len(categorias) == 0: 
            st.write("Nenhuma categoria cadastrada")
        else:    
            list_dic = [obj.__dict__ for obj in categorias]
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descrição da categoria:")
        if st.button("Cadastrar"):
            try:
                View.categoria_inserir(descricao)
                st.success("Categoria inserida com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(f"Erro: {erro}")
                time.sleep(2)
                st.rerun()

    def atualizar():
        categorias = View.categoria_listar()
        if len(categorias) == 0: 
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Atualização de categoria", categorias)
            nova_descricao = st.text_input("Informe a nova descrição", op.getDescricao())
            if st.button("Atualizar"):
                try:
                    View.categoria_atualizar(op.getId(), nova_descricao)
                    st.success("Categoria atualizada com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(f"Erro: {erro}")
                    time.sleep(2)
                    st.rerun()

    def excluir():
        categorias = View.categoria_listar()
        if len(categorias) == 0: 
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Exclusão de categoria", categorias)
            if st.button("Excluir"):
                try:
                    View.categoria_excluir(op.getId())
                    st.success("Categoria excluída com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(f"Erro: {erro}")
                    time.sleep(2)
                    st.rerun()
