import streamlit as st
import pandas as pd
from View.views import View
import time

class ManterEntregadorUI:
    def main():
        st.header("Gerenciamento de Entregadores")
        tab1, tab2, tab3 = st.tabs(["Listar", "Inserir", "Atualizar"])
        with tab1: ManterEntregadorUI.listar()
        with tab2: ManterEntregadorUI.inserir()
        with tab3: ManterEntregadorUI.atualizar()

    def listar():
        entregadores = View.entregador_listar()
        if len(entregadores) == 0:
            st.write("Nenhum entregador cadastrado")
        else:
            list_dic = []
            for obj in entregadores:
                dic_entregador = obj.__dict__.copy()
                if "senha" in dic_entregador:
                    del dic_entregador["senha"]
                if dic_entregador["_Entregador__status"] == True:
                    dic_entregador["_Entregador__status"] = "Em serviço"
                else:
                    dic_entregador["_Entregador__status"] = "Disponível"
                list_dic.append(dic_entregador)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o e-mail: ")
        fone = st.text_input("Informe o fone: ")
        if st.button("Cadastrar"):
            try:
                View.entregador_inserir(nome, email, "1234")
                st.success("Entregador inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
                time.sleep(2)
                st.rerun()

    def atualizar():
        entregadores = View.entregador_listar()
        if len(entregadores) == 0:
            st.write("Nenhum entregador cadastrado")
        else:
            op = st.selectbox("Atualização de entregador", entregadores)
            nome = st.text_input("Informe o novo nome", op.getNome())
            email = st.text_input("Informe o novo e-mail", op.getEmail())
            if st.button("Atualizar"):
                try:
                    View.entregador_atualizar(op.getId(), nome, email, op.getSenha())
                    st.success("Entregador atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                    time.sleep(2)
                    st.rerun()

    def listarPedidosPendentes():
        pedidos = View.listar_minhas_entregas(st.session_state["usuario_id"])
        if len(pedidos) == 0:
            st.write("Nenhum entrega pendente")
        else:
            list_dic = [{"id": p.getId(), "data": p.getData(), "total": p.getTotal(), "id_cliente": p.getIdCliente(), "status_envio": p.getStatusEnvio()[0]} for p in pedidos]
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def confirmarEntrega():
        pedidos = View.listar_minhas_entregas(st.session_state["usuario_id"])
        if len(pedidos) == 0:
            st.write("Nenhum entrega pendente")
        else:
            op = st.selectbox("Selecione o Pedido", pedidos)
            if st.button("Confirmar Entrega"):
                try:
                    View.pedido_atualizar_status_envio(op.getId(), "Entregue", 0)
                    st.success("Entrega confirmada com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                    time.sleep(2)
                    st.rerun()
    
