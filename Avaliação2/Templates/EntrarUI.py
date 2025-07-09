import streamlit as st
from views import View

class EntrarUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            c = View.autenticacao_Usuario(email, senha)
            if c == None: 
                st.write("E-mail ou senha inválidos")
            else:    
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
                st.rerun()
               