import streamlit as st
from datetime import datetime, time
from pydantic import ValidationError

from contrato import Vendas
from database import salvar_dados_no_postgres

def main():
    st.title("titulo da janela")

    email = st.text_input("E-mail do vendedor")
    data = st.date_input("Data da venda", datetime.now())
    hora = st.time_input("Hora da venda", value=time(9,0))
    valor = st.number_input("Valor do produto", min_value=0.0, format="%.2f")
    qtde = st.number_input("Qtde vendida", min_value=1, step=1)
    produtoVendido = st.selectbox("Produto vendido",["Produto A", "Produto B", "Produto C"])

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(email = email, data = data_hora, 
                           valor = valor, qtde = qtde, 
                           produto = produtoVendido)

            st.write(venda)

            salvar_dados_no_postgres(venda)

        except ValidationError as e:
            st.error(f"Deu ruim {e}")

        # st.write(email)
        # st.write(data_hora)
        # st.write(produtoVendido)
        # st.write(qtde)
        # st.write(valor)



if __name__ == "__main__":
    main()