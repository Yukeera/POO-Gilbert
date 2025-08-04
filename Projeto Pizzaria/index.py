import streamlit as st
from View.views import View
from Templates.ManterCategoriaUI import ManterCategoriaUI
from Templates.ManterClienteUI import ManterClienteUI
from Templates.ManterProdutoUI import ManterProdutoUI
from Templates.ManterPedidosUI import ManterPedidosUI
from Templates.ManterEntregadorUI import ManterEntregadorUI
from Templates.EntrarUI import EntrarUI
from Templates.AbrirContaUI import AbrirContaUI

class IndexUI:
    def menu_visitante():
        st.header("Bem-vindo ao Sistema de Pizzaria")
        st.write("Por favor, faça login ou crie uma conta para continuar.")
        st.write("Você pode navegar pelo menu à esquerda.")
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": EntrarUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Categorias", "Cadastro de Clientes", "Cadastro de Produtos", "Listagem de Vendas", "Cadastro de Entregadores", "Despachar Pedidos"])
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Listagem de Vendas": ManterPedidosUI.listarAdmin()
        if op == "Cadastro de Entregadores": ManterEntregadorUI.main()
        if op == "Despachar Pedidos": ManterPedidosUI.despachar_pedido()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Mostrar Cardápio", "Adicionar Produto no Pedido", "Ver Carrinho", "Confirmar Pedido", "Ver Minhas Compras"])
        if op == "Mostrar Cardápio": ManterProdutoUI.listar()
        if op == "Adicionar Produto no Pedido": ManterPedidosUI.inserirProdutoNoPedido()
        if op == "Ver Carrinho": ManterPedidosUI.verMeuPedido()
        if op == "Confirmar Pedido": ManterPedidosUI.confirmarCompra()
        if op == "Ver Minhas Compras": ManterClienteUI.listarCompras()

    def menu_entregador():
        op = st.sidebar.selectbox("Menu", ["Ver Pedidos Pendentes", "Confirmar Entrega"])
        if op == "Ver Pedidos Pendentes": ManterEntregadorUI.listarPedidosPendentes()
        if op == "Confirmar Entrega": ManterEntregadorUI.confirmarEntrega()
        




    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        #st.write(st.session_state)
        if "usuario_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["usuario_nome"] == "admin"
            entregador = st.session_state["usuario_tipo"] == "Entregador"
            # mensagem de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            # menu do usuário
            if admin: IndexUI.menu_admin()
            elif entregador: IndexUI.menu_entregador()
            else: IndexUI.menu_cliente()
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 
    
    def main():
        # verifica a existe o usuário admin
        View.cadastrar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()