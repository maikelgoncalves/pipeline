import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

#carregar as variaveis do arquivo .env
load_dotenv()

#atribui a variaveis as chaves que estão no .env
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")
db_user = os.getenv("db_user")
db_pwd = os.getenv("db_pwd")

def salvar_dados_no_postgres(dados: Vendas):
    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pwd
        )

        cursor = conn.cursor()

        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, qtde, produto) VALUES (%s, %s, %s, %s, %s)"
        )

        cursor.execute(insert_query, (
            dados.email, dados.data, dados.valor, dados.qtde, dados.produto.value
        ))

        conn.commit()
        cursor.close()
        conn.close()

        st.success("Dados salvos no DB com sucesso \\o/")
    except Exception as e:
        st.error(f"Erro ao salvar no DB: {e}")