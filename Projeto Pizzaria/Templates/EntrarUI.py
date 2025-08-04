import streamlit as st
from View.views import View
import time

class EntrarUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            usuario = View.usuario_autenticar(email, senha)
            if usuario is None: 
                st.error("E-mail ou senha inválidos")
            else:    
                st.session_state["usuario"] = usuario
                st.session_state["usuario_id"] = usuario.getId()
                st.session_state["usuario_nome"] = usuario.getNome()
                st.session_state["usuario_tipo"] = usuario.getType()
                st.success("Login realizado com sucesso!")
                time.sleep(2)
                st.rerun()
