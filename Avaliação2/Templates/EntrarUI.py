import streamlit as st
from views import View
import time

class EntrarUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            cliente = View.cliente_autenticar(email, senha)
            if cliente is None: 
                st.error("E-mail ou senha inválidos")
            else:    
                st.session_state["cliente"] = cliente
                st.session_state["cliente_id"] = cliente.getId()
                st.session_state["cliente_nome"] = cliente.getNome()
                View.clienteCarrinhoCC(cliente.getId())
                venda_id = View.clienteCarrinhoCC(cliente.getId())
                st.session_state["venda_id"] = venda_id 
                st.success("Login realizado com sucesso!")
                time.sleep(2)
                st.rerun()
