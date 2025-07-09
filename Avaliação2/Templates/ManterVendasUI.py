import streamlit as st
import pandas as pd
from views import View
import time

class ManterVendasUI:
    def main():
        st.header("Compras dos Clientes")
        tab1 = st.tabs(["Listar Compras"])[0]
        with tab1:
            ManterVendasUI.listar()

    def listar():
        vendas = View.listar_vendas_admin()
        if len(vendas) == 0:
            st.write("Nenhuma compra foi realizada ainda.")
        else:
            list_dic = []
            for venda in vendas:
                list_dic.append({
                    "Cliente ID": venda["cliente_id"],
                    "Cliente Nome": venda["cliente_nome"],
                    "Descrição da Compra": venda["descricao"]
                })
            df = pd.DataFrame(list_dic)
            st.dataframe(df)