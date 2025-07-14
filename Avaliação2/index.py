import streamlit as st
from views import View
from Templates.ManterCategoriaUI import ManterCategoriaUI
from Templates.ManterClienteUI import ManterClienteUI
from Templates.ManterProdutoUI import ManterProdutoUI
from Templates.ManterVendasUI import ManterVendasUI
from Templates.EntrarUI import EntrarUI
from Templates.AbrirContaUI import AbrirContaUI

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": EntrarUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Categorias", "Cadastro de Clientes", "Cadastro de Produtos", "Listagem de Vendas"])
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Listagem de Vendas": ManterVendasUI.listarAdmin()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Listar Produtos", "Adicionar Produto no Carrinho", "Ver Carrinho", "Confirmar Compra", "Ver Minhas Compras", "Comprar Novamente"])
        if op == "Listar Produtos": ManterProdutoUI.listar()
        if op == "Adicionar Produto no Carrinho": ManterVendasUI.inserirProdutoNoCarrinho()
        if op == "Ver Carrinho": ManterVendasUI.verMeuCarrinho()
        if op == "Confirmar Compra": ManterVendasUI.confirmarCompra()
        if op == "Ver Minhas Compras": ManterClienteUI.listarCompras()
        if op == "Comprar Novamente": ManterVendasUI.tela_comprar_novamente()
            



    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()

    def sidebar():
        #st.write(st.session_state)
        if "cliente_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["cliente_nome"] == "admin"
            # mensagem de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            # menu do usuário
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 
    
    def main():
        # verifica a existe o usuário admin
        View.cadastrar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()
