import streamlit as st
import pandas as pd
from views import View

class ManterVendasUI:
    def main():
        st.header("Compras dos Clientes")
        tab1 = st.tabs(["Listar Compras"])[0]
        with tab1:
            ManterVendasUI.listar()

    def listar():
        vendas = View.venda_listar_admin()
        if len(vendas) == 0:
            st.write("Nenhuma compra foi realizada ainda.")
        else:
            df = pd.DataFrame(vendas)
            st.dataframe(df)
