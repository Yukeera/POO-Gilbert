import streamlit as st
from views import View
import time
from Templates.EntrarUI import EntrarUI

class AbrirContaUI:
    def main():
        st.header("Abrir Conta")
        nome = st.text_input("Informe o seu nome")
        email = st.text_input("Informe o seu email")
        senha = st.text_input("Informe sua senha", type="password")
        fone = st.text_input("informe seu Telefone")
        if st.button("Criar conta!"):
            View.cliente_inserir(nome, email, senha, fone)
            st.success("Conta criada com sucesso. Faça o login.")
            time.sleep(2)
            st.rerun()